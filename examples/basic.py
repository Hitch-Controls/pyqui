import sys

from pyqui import PQApplication
from pyqui.gui.main_window import PQMainWindow


class MyApplication(PQApplication):
    app_name = "My Basic Application"
    version = "v1.0.0"
    organization = "Made With PyQui"
    app_icon = "$RES_PATH/icon.ico"
    app_logo = "logo_top_100x22.svg"
    app_logo_width = 100
    default_theme_name = "default"
    year = '2000'


class MyMainWindow(PQMainWindow):
    def _init_widgets(self):
        super()._init_widgets()


if __name__ == "__main__":
    app = MyApplication(sys.argv, main_window_cls=MyMainWindow)
    sys.exit(app.exec())