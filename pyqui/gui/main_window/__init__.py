import sys


if sys.platform == 'win32':
    from pyqui.platform.win32.main_window import PQWin32MainWindow as PQMainWindow
    from pyqui.platform.win32.main_window import PQWin32FramelessMainWindow as PQFramelessMainWindow
elif sys.platform == 'darwin':
    from pyqui.platform.darwin.main_window import PQDarwinMainWindow as PQMainWindow
    from pyqui.platform.darwin.main_window import PQDarwinFramelessMainWindow as PQFramelessMainWindow
else:
    from .core import PQMainWindow
    from .frameless import PQFramelessMainWindow
