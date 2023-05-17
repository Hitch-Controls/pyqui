# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import os
import sys
import typing
import logging
from datetime import date

from pyqui.resources.utils import *
from pyqui.conf import get_settings
from pyqui.gui.uis.columns.ui_right_column import Ui_RightColumn
from pyqui.qt import qtw, qtc, qtg

from pyqui.gui.widgets import PQCreditsBar, PyTitleBar, PyLeftMenu, PyLeftColumn, PQWindow

from .utils import MainWindowUtils


if typing.TYPE_CHECKING:
    from pyqui.app import PQApplication

# ADJUST QT FONT DPI FOR HIGHT SCALE AN 4K MONITOR
# ///////////////////////////////////////////////////////////////
# os.environ["QT_FONT_DPI"] = "96"
# IF IS 4K MONITOR ENABLE 'os.environ["QT_SCALE_FACTOR"] = "2"'

logger = logging.getLogger(__name__)


class PQMainWindow(qtw.QMainWindow, MainWindowUtils):

    def __init__(self, parent=None, *args, app=None, **kwargs):
        super().__init__(*args, **kwargs)

        self.app = app
        self.settings = get_settings()
        self.themes = self.settings.theme

        self._init_window()
        self._init_widgets()

        self.resize(self.settings["startup_size"][0], self.settings["startup_size"][1])
        self.setMinimumSize(self.settings["minimum_size"][0], self.settings["minimum_size"][1])

    def _init_window(self):
        if not self.objectName():
            self.setObjectName("DSMainWindow")

    def _init_widgets(self):
        self.central_widget = qtw.QWidget()
        self.central_widget_layout = qtw.QVBoxLayout(self.central_widget)
        self.central_widget_layout.setContentsMargins(0, 0, 0, 0)
        self.setCentralWidget(self.central_widget)
