from pyqui.qt import *
from pyqui.gui.main_window.core import PQMainWindow


class PQDarwinMainWindow(PQMainWindow):
    def _init_widgets(self):
        super()._init_widgets()
        self.title_bar.drag_pos.connect(self._handle_window_drag)
