# ///////////////////////////////////////////////////////////////
#
# ///////////////////////////////////////////////////////////////
#
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

from pyqui.qt import *
from pyqui.conf import get_settings


style = """
#PyQuiWindow {{
    background-color: {background_color};
    border-radius: {border_radius};
    border: {border_size}px solid {border_color};
}}
"""


class PQWindow(qtw.QFrame):
    theme_settings = {
        'background_color': 'bg_one',
        'border_color': 'bg_two',
        'border_size': 2,
        'border_radius': 10,
    }

    def __init__(self, parent):
        super().__init__(parent=parent)
        self.setObjectName("PyQuiWindow")
        self.settings = get_settings()

        layout = qtw.QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(2)

        # If disable custom title bar
        if not self.settings["custom_title_bar"]:
            self.set_stylesheet(border_radius=0, border_size=0)
        else:
            self.set_stylesheet()

    def set_stylesheet(self, **kwargs):
        fmt_opts = {
            setting: self.settings.theme['app_color'].get(default, default) for setting, default in self.theme_settings.items()
        }
        fmt_opts.update(kwargs)
        self.setStyleSheet(style.format(**fmt_opts))
