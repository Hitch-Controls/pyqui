import sys
import ctypes
import win32api
import win32gui
import win32con
from ctypes.wintypes import LONG

from pyqui.qt import *
from pyqui.ui.mainwindow.core import PQMainWindow
from pyqui.ui.mainwindow.frameless import PQFramelessMainWindow

from . import utils


class PQWin32MainWindow(PQMainWindow):
    pass


class PQWin32FramelessMainWindow(PQFramelessMainWindow):
    def _init_window(self):
        super()._init_window()
        
        if sys.platform == 'win32':
            hwnd = int(self.winId())
            window_style = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)
            win32gui.SetWindowLong(
                hwnd,
                win32con.GWL_STYLE,
                window_style
                | win32con.WS_CAPTION
                | win32con.WS_THICKFRAME
                | win32con.WS_SYSMENU
                | win32con.WS_MAXIMIZEBOX
                | win32con.WS_MINIMIZEBOX
            )
            # win32gui.SetWindowPos(hwnd, win32con.NULL, 0, 0, 0, 0, win32con.SWP_FRAMECHANGED)
                
    def nativeEvent(self, eventType, message):
        _edge_test_width = 8

        if eventType == b"windows_generic_MSG":
            msg = ctypes.wintypes.MSG.from_address(message.__int__())
            if msg.message == win32con.WM_NCCALCSIZE:
                # handles redrawing on resize
                result = 0 if not msg.wParam else win32con.WVR_REDRAW
                return True, result
            elif msg.message == win32con.WM_SYSKEYDOWN:
                # Handle Alt+F4 cleanly
                if msg.wParam == win32con.VK_F4:
                    qtw.QApplication.sendEvent(self, qtg.QCloseEvent())
                    return False, 0
            elif msg.message == win32con.WM_NCHITTEST:
                # Handles window moving and resizing
                fg = self.frameGeometry()
                title_bar_rect = self.title_bar.drag_rect()
                title_bar_rect.moveTo(title_bar_rect.x()-fg.x(), title_bar_rect.y()-fg.y())

                x = (win32api.LOWORD(LONG(msg.lParam).value) - self.frameGeometry().x()) % 65536
                y = (win32api.HIWORD(LONG(msg.lParam).value) - self.frameGeometry().y()) % 65536

                # resize grip test return True and the position if the mouse is in a window group region
                w, h = self.width(), self.height()
                lx = x < _edge_test_width
                rx = x > w - _edge_test_width
                ty = y < _edge_test_width
                by = y > h - _edge_test_width
                if lx and ty:
                    return True, win32con.HTTOPLEFT
                if rx and by:
                    return True, win32con.HTBOTTOMRIGHT
                if rx and ty:
                    return True, win32con.HTTOPRIGHT
                if lx and by:
                    return True, win32con.HTBOTTOMLEFT
                if ty:
                    return True, win32con.HTTOP
                if by:
                    return True, win32con.HTBOTTOM
                if lx:
                    return True, win32con.HTLEFT
                if rx:
                    return True, win32con.HTRIGHT
                if title_bar_rect.contains(x, y):
                    # Drag the window from the title bar
                    return True, win32con.HTCAPTION
            elif msg.message == win32con.WM_EXITSIZEMOVE:
                # TODO:
                #  This is a workaround for moving the window between different dpi/resolutions. by triggering a resize
                #  Qt figures its life out and things start redrawing correctly. This does sometimes cause the window
                #  to shrink/grow slightly (thanks windows?) - cant be bothered enough to figure out the "right"
                #  solution for this at the moment - ventorvar
                rect = win32gui.GetWindowRect(self.winId())
                self.resize(rect[2]-rect[0], rect[3]-rect[1])

        return super().nativeEvent(eventType, message)
