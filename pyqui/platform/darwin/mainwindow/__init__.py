from pyqui.qt import *
from pyqui.ui.mainwindow.core import PQMainWindow
from pyqui.ui.mainwindow.frameless import PQFramelessMainWindow


class PQDarwinMainWindow(PQMainWindow):
    pass


class PQDarwinFramelessMainWindow(PQFramelessMainWindow):
    def _init_widgets(self):
        super()._init_widgets()
        self.title_bar.drag_pos.connect(self._handle_window_drag)
