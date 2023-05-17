import sys


if sys.platform == 'win32':
    from pyqui.platform.win32.main_window import PQWin32MainWindow as PQMainWindow
elif sys.platform == 'darwin':
    from pyqui.platform.darwin.main_window import PQDarwinMainWindow as PQMainWindow
else:
    from .core import PQMainWindow
