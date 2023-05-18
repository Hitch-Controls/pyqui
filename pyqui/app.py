from datetime import date

from pyqui.qt import qtw, qtc, qtg
from pyqui.ui.mainwindow import PQMainWindow
from pyqui.conf.settings import get_settings, Settings
from pyqui.resources import RES_PATH


class PQApplication(qtw.QApplication):
    app_name = "PyQui - Python Qt Desktop Application Framework"
    version = "v1.0.0"
    organization = "Made With PyQui"
    app_icon = "$RES_PATH/icon.ico"
    app_logo = "logo_top_100x22.svg"
    app_logo_width = 100
    default_theme_name = "default"
    year = date.year

    theme_updated = qtc.Signal()

    def __new__(cls, *args, **kwargs):
        qtw.QApplication.setAttribute(qtc.Qt.AA_EnableHighDpiScaling)
        qtw.QApplication.setAttribute(qtc.Qt.AA_UseHighDpiPixmaps)
        qtw.QApplication.setHighDpiScaleFactorRoundingPolicy(qtc.Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
        return super().__new__(cls)

    def __init__(self, *args, main_window_cls=PQMainWindow, settings_cls=Settings, **kwargs):
        super().__init__(*args, **kwargs)

        self.settings: settings_cls = get_settings(cls=settings_cls)
        self.settings.theme.signals.theme_changed.connect(self._handle_theme_changed)
        self._main_window_cls = main_window_cls
        self.main_window = None

        self.setOrganizationName(self.organization)
        self.setApplicationDisplayName(self.app_name)
        self.setWindowIcon(qtg.QIcon(self.app_icon.replace("$RES_PATH", RES_PATH.as_posix())))

        self._handle_theme_changed()

    def _handle_theme_changed(self):
        self.setStyleSheet(self.settings.theme.qt_stylesheet())
        self.theme_updated.emit()

    def exec(self):
        self.main_window = self._main_window_cls(app=self)
        self.main_window.setWindowTitle(self.app_name)
        self.main_window.show()
        return super().exec()

    def shutdown(self):
        if self.main_window is not None:
            self.main_window.destroy()
        super().shutdown()


def get_app() -> PQApplication:
    return qtw.QApplication.instance()
