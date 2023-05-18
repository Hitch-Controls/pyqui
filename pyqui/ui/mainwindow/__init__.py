import sys


if sys.platform == 'win32':
    from pyqui.platform.win32.mainwindow import PQWin32MainWindow as PQMainWindow
    from pyqui.platform.win32.mainwindow import PQWin32FramelessMainWindow as PQFramelessMainWindow
elif sys.platform == 'darwin':
    from pyqui.platform.darwin.mainwindow import PQDarwinMainWindow as PQMainWindow
    from pyqui.platform.darwin.mainwindow import PQDarwinFramelessMainWindow as PQFramelessMainWindow
else:
    from .core import PQMainWindow
    from .frameless import PQFramelessMainWindow
