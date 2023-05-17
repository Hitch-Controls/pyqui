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
import typing
from pathlib import Path

from pyqui.conf.themes import ThemeManager


class Settings(dict):
    def __init__(self, theme_managr_cls=ThemeManager, *args, **kwargs):
        super().__init__()
        self.load_settings(Path(__file__).parent / "default_settings.json")
        self.update(dict(*args, **kwargs))
        self.theme = theme_managr_cls(self)

    def load_settings(self, settings_path: typing.Union[str, Path], clean=False):
        settings_path = Path(settings_path)
        if clean:
            self.clear()
        with settings_path.open("r", encoding="utf-8") as f:
            self.update(json.load(f))

    def save_settings(self, settings_path: typing.Union[str, Path]):
        settings_path = Path(settings_path)
        with settings_path.open("w", encoding="utf-8") as f:
            json.dump(self, f, indent=4)


_settings = None


def get_settings(cls=Settings):
    global _settings
    if _settings is None:
        _settings = cls()
    return _settings
