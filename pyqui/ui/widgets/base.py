from pyqui.qt import qtw
from pyqui.conf import get_settings


class ThemedWidget(qtw.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

