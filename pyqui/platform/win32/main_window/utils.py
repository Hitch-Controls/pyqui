import ctypes
import win32api
import win32gui
import win32con
from ctypes import Structure, byref, sizeof, windll, c_int
from ctypes.wintypes import DWORD, HWND, LPARAM, RECT, UINT

import win32api
import win32con
import win32gui
from win32comext.shell import shellcon

from pyqui.qt.QtCore import QOperatingSystemVersion
from pyqui.qt.QtGui import QGuiApplication


def isMaximized(hWnd):
    """ Determine whether the window is maximized
    Parameters
    ----------
    hWnd: int or `sip.voidptr`
        window handle
    """
    windowPlacement = win32gui.GetWindowPlacement(hWnd)
    if not windowPlacement:
        return False

    return windowPlacement[1] == win32con.SW_MAXIMIZE


def isFullScreen(hWnd):
    """ Determine whether the window is full screen
    Parameters
    ----------
    hWnd: int or `sip.voidptr`
        window handle
    """
    if not hWnd:
        return False

    hWnd = int(hWnd)
    winRect = win32gui.GetWindowRect(hWnd)
    if not winRect:
        return False

    monitorInfo = getMonitorInfo(hWnd, win32con.MONITOR_DEFAULTTOPRIMARY)
    if not monitorInfo:
        return False

    monitorRect = monitorInfo["Monitor"]
    return all(i == j for i, j in zip(winRect, monitorRect))


def getMonitorInfo(hWnd, dwFlags):
    """ get monitor info, return `None` if failed
    Parameters
    ----------
    hWnd: int or `sip.voidptr`
        window handle
    dwFlags: int
        Determines the return value if the window does not intersect any display monitor
    """
    monitor = win32api.MonitorFromWindow(hWnd, dwFlags)
    if not monitor:
        return

    return win32api.GetMonitorInfo(monitor)


def getResizeBorderThickness(hWnd):
    """ get resize border thickness of widget
    Parameters
    ----------
    hWnd: int or `sip.voidptr`
        window handle
    dpiScale: bool
        whether to use dpi scale
    """
    window = findWindow(hWnd)
    if not window:
        return 0

    result = win32api.GetSystemMetrics(
        win32con.SM_CXSIZEFRAME) + win32api.GetSystemMetrics(92)

    if result > 0:
        return result

    thickness = 8 if IsCompositionEnabled() else 4
    return round(thickness * window.devicePixelRatio())


def findWindow(hWnd):
    """ find window by hWnd, return `None` if not found
    Parameters
    ----------
    hWnd: int or `sip.voidptr`
        window handle
    """
    if not hWnd:
        return

    windows = QGuiApplication.topLevelWindows()
    if not windows:
        return

    hWnd = int(hWnd)
    for window in windows:
        if window and int(window.winId()) == hWnd:
            return window


def IsCompositionEnabled():
    """ detect if dwm composition is enabled """
    bResult = c_int(0)
    windll.dwmapi.DwmIsCompositionEnabled(byref(bResult))
    return bool(bResult.value)


def isGreaterEqualVersion(version):
    """ determine if the windows version ≥ the specifics version
    Parameters
    ----------
    version: QOperatingSystemVersion
        windows version
    """
    return QOperatingSystemVersion.current() >= version


def isGreaterEqualWin8_1():
    """ determine if the windows version ≥ Win8.1 """
    return isGreaterEqualVersion(QOperatingSystemVersion.Windows8_1)


class APPBARDATA(Structure):
    _fields_ = [
        ('cbSize', DWORD),
        ('hWnd', HWND),
        ('uCallbackMessage', UINT),
        ('uEdge', UINT),
        ('rc', RECT),
        ('lParam', LPARAM),
    ]
