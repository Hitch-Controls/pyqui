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

import json
import logging
from importlib import resources

from pyqui.qt import qtc
from pyqui.resources import RES_PATH

logger = logging.getLogger(__name__)


class ThemeSignals(qtc.QObject):
    theme_changed = qtc.Signal()


class ThemeManager(dict):
    THEMES_PATH = RES_PATH / "themes"
    AVAILABLE_THEMES = list(THEMES_PATH.glob('*.json'))

    def __init__(self, settings):
        super(ThemeManager, self).__init__()

        self.settings = settings
        self.signals = ThemeSignals()
        self.current_theme_name = ''
        theme = settings.get('theme_name', 'default')
        try:
            self.load_theme(theme)
        except Exception as e:
            logger.warning(f'Error loading theme "{theme}": {e}')
            self.load_theme('default')

    def qt_stylesheet(self):
        template = resources.read_text("pyqui.resources", "template.qss")
        return template.format(
            common_text_size=self.settings["font"]["text_size"],
            common_font_family=self.settings["font"]["family"],
            common_text_foreground=self["app_color"]["text_foreground"],

            qslider_margin=8,
            qslider_bg_size=10,
            qslider_bg_radius=5,
            qslider_handle_margin=-3,
            qslider_handle_size=16,
            qslider_handle_radius=8,
            qslider_bg_color=self["app_color"]["dark_three"],
            qslider_bg_color_hover=self["app_color"]["dark_four"],
            qslider_handle_color=self["app_color"]["context_color"],
            qslider_handle_color_hover=self["app_color"]["context_hover"],
            qslider_handle_color_pressed=self["app_color"]["context_pressed"],

            qpushbutton_radius=8,
            qpushbutton_color=self["app_color"]["text_foreground"],
            qpushbutton_bg_color=self["app_color"]["dark_one"],
            qpushbutton_bg_color_hover=self["app_color"]["dark_three"],
            qpushbutton_bg_color_pressed=self["app_color"]["dark_four"],

            qlineedit_radius=8,
            qlineedit_border_size=2,
            qlineedit_color=self["app_color"]["text_foreground"],
            qlineedit_selection_color=self["app_color"]["white"],
            qlineedit_bg_color=self["app_color"]["dark_one"],
            qlineedit_bg_color_active=self["app_color"]["dark_three"],
            qlineedit_context_color=self["app_color"]["context_color"],

            qtableview_radius=8,
            qtableview_color=self["app_color"]["text_foreground"],
            qtableview_selection_color=self["app_color"]["context_color"],
            qtableview_bg_color=self["app_color"]["bg_two"],
            qtableview_header_horizontal_color=self["app_color"]["dark_two"],
            qtableview_header_vertical_color=self["app_color"]["bg_three"],
            qtableview_bottom_line_color=self["app_color"]["bg_three"],
            qtableview_grid_line_color=self["app_color"]["bg_one"],
            qtableview_alternate_background_color=self["app_color"]["bg_one"],

            qscrollbar_bg_color=self["app_color"]["bg_one"],
            qscrollbar_btn_color=self["app_color"]["dark_four"],
            qscrollbar_context_color=self["app_color"]["context_color"],
        )

    def save_theme(self, name):
        with (self.THEMES_PATH / name).with_suffix('.json').open('w') as f:
            json.dump(self, f, indent=4)

    def load_theme(self, name, clear=False):
        if clear:
            self.clear()
        with (theme_file := (self.THEMES_PATH / name).with_suffix('.json')).open('r', encoding="utf-8") as f:
            self.update(json.load(f))
            self.current_theme_name = theme_file.stem
            self.signals.theme_changed.emit()

