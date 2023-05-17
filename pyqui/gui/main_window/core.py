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

from pyqui.gui.widgets import PQCreditsBar, PyTitleBar, PyLeftMenu, PyLeftColumn, PQWindow, PQGrips

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

        if self.settings["custom_title_bar"]:
            self.setWindowFlag(qtc.Qt.FramelessWindowHint)
            self.setAttribute(qtc.Qt.WA_TranslucentBackground)

    def _init_qt_grips(self):
        # ADD GRIPS
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.window_grips = PQGrips(self)

    def _init_widgets(self):
        self.central_widget = qtw.QWidget()
        self.central_widget_layout = qtw.QVBoxLayout(self.central_widget)
        # if self.settings["custom_title_bar"]:
        #     self.central_widget_layout.setContentsMargins(10, 10, 10, 10)
        # else:
        #     self.central_widget_layout.setContentsMargins(0, 0, 0, 0)
        self.central_widget_layout.setContentsMargins(0, 0, 0, 0)

        self.window = PQWindow(self)
        self.central_widget_layout.addWidget(self.window)

        ########################################
        # region: left_menu
        left_menu_margin = self.settings["left_menu_content_margins"]
        left_menu_minimum = self.settings["lef_menu_size"]["minimum"]
        self.left_menu_frame = qtw.QFrame()
        self.left_menu_frame.setMaximumSize(left_menu_minimum + (left_menu_margin * 2), 17280)
        self.left_menu_frame.setMinimumSize(left_menu_minimum + (left_menu_margin * 2), 0)

        self.left_menu_layout = qtw.QHBoxLayout(self.left_menu_frame)
        self.left_menu_layout.setContentsMargins(left_menu_margin, left_menu_margin, left_menu_margin, left_menu_margin)

        self.left_menu = PyLeftMenu(
            parent=self.left_menu_frame,
            app_parent=self.central_widget,  # For tooltip parent
            dark_one=self.themes["app_color"]["dark_one"],
            dark_three=self.themes["app_color"]["dark_three"],
            dark_four=self.themes["app_color"]["dark_four"],
            bg_one=self.themes["app_color"]["bg_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["icon_pressed"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            context_color=self.themes["app_color"]["context_color"],
            text_foreground=self.themes["app_color"]["text_foreground"],
            text_active=self.themes["app_color"]["text_active"],
        )
        self.left_menu_layout.addWidget(self.left_menu)
        self.left_menu.clicked.connect(self.btn_clicked)
        self.left_menu.released.connect(self.btn_released)
        # endregion: left_menu
        ########################################

        ########################################
        # region: left
        # ADD LEFT COLUMN
        # Add here the left column with Stacked Widgets
        # ///////////////////////////////////////////////////////////////
        self.left_column_frame = qtw.QFrame()
        self.left_column_frame.setMaximumWidth(self.settings["left_column_size"]["minimum"])
        self.left_column_frame.setMinimumWidth(self.settings["left_column_size"]["minimum"])
        self.left_column_frame.setStyleSheet(f"background: {self.themes['app_color']['bg_two']}")

        # ADD LAYOUT TO LEFT COLUMN
        self.left_column_layout = qtw.QVBoxLayout(self.left_column_frame)
        self.left_column_layout.setContentsMargins(0, 0, 0, 0)

        # ADD CUSTOM LEFT MENU WIDGET
        self.left_column = PyLeftColumn(
            self,
            app_parent=self.central_widget,
            text_title="Settings Left Frame",
            text_title_size=self.settings["font"]["title_size"],
            text_title_color=self.themes["app_color"]["text_foreground"],
            icon_path=svg_icon("icon_settings.svg"),
            dark_one=self.themes["app_color"]["dark_one"],
            bg_color=self.themes["app_color"]["bg_three"],
            btn_color=self.themes["app_color"]["bg_three"],
            btn_color_hover=self.themes["app_color"]["bg_two"],
            btn_color_pressed=self.themes["app_color"]["bg_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            context_color=self.themes["app_color"]["context_color"],
            icon_color_pressed=self.themes["app_color"]["icon_pressed"],
            icon_close_path=svg_icon("icon_close.svg"),
        )
        self.left_column_layout.addWidget(self.left_column)
        self.left_column.clicked.connect(self.btn_clicked)
        self.left_column.released.connect(self.btn_released)
        # endregion: left
        ########################################

        ########################################
        # right side "main" area
        self.right_app_frame = qtw.QFrame()
        self.right_app_layout = qtw.QVBoxLayout(self.right_app_frame)
        self.right_app_layout.setContentsMargins(3, 3, 3, 3)
        self.right_app_layout.setSpacing(6)

        ########################################
        # region: title bar
        # right side "main" area
        # ADD TITLE BAR FRAME
        # ///////////////////////////////////////////////////////////////
        self.title_bar_frame = qtw.QFrame()
        self.title_bar_frame.setMinimumHeight(40)
        self.title_bar_frame.setMaximumHeight(40)
        self.title_bar_layout = qtw.QVBoxLayout(self.title_bar_frame)
        self.title_bar_layout.setContentsMargins(0, 0, 0, 0)

        # ADD CUSTOM TITLE BAR TO LAYOUT
        self.title_bar = PyTitleBar(
            self,
            app_parent=self.central_widget,
            logo_image=self.app.app_logo,
            bg_color=self.themes["app_color"]["bg_two"],
            div_color=self.themes["app_color"]["bg_three"],
            btn_bg_color=self.themes["app_color"]["bg_two"],
            btn_bg_color_hover=self.themes["app_color"]["bg_three"],
            btn_bg_color_pressed=self.themes["app_color"]["bg_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["icon_pressed"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            context_color=self.themes["app_color"]["context_color"],
            dark_one=self.themes["app_color"]["dark_one"],
            text_foreground=self.themes["app_color"]["text_foreground"],
            radius=8,
            font_family=self.settings["font"]["family"],
            title_size=self.settings["font"]["title_size"],
            is_custom_title_bar=self.settings["custom_title_bar"],
        )
        self.title_bar_layout.addWidget(self.title_bar)
        self.title_bar.clicked.connect(self.btn_clicked)
        self.title_bar.released.connect(self.btn_released)

        # ADD Title
        if self.settings["custom_title_bar"]:
            self.title_bar.set_title(self.app.app_name)
        # endregion: title bar
        ########################################

        ########################################
        # region: content
        # ADD CONTENT AREA
        self.content_area_frame = qtw.QFrame(parent=self.right_app_frame)
        # self.content_area_frame.setStyleSheet("background: blue")

        # CREATE LAYOUT
        self.content_area_layout = qtw.QHBoxLayout()
        self.content_area_layout.setContentsMargins(0, 0, 0, 0)
        self.content_area_layout.setSpacing(0)
        self.content_area_frame.setLayout(self.content_area_layout)

        # LEFT CONTENT
        self.content_area_left_frame = qtw.QFrame(parent=self.content_area_frame)
        self.content_area_left_frame.setObjectName("MainPages")
        self.content_area_left_frame.resize(860, 600)
        main_pages_layout = qtw.QVBoxLayout()
        main_pages_layout.setSpacing(0)
        main_pages_layout.setObjectName("main_pages_layout")
        main_pages_layout.setContentsMargins(0, 0, 0, 0)
        self.content_area_left_frame.setLayout(main_pages_layout)
        self.content_area_layout.addWidget(self.content_area_left_frame)

        self.stacked_pages = qtw.QStackedWidget(self.content_area_left_frame)
        self.stacked_pages.setObjectName(u"pages")
        main_pages_layout.addWidget(self.stacked_pages)

        # RIGHT BAR
        self.right_column_frame = qtw.QFrame()
        self.right_column_frame.setMinimumWidth(self.settings["right_column_size"]["minimum"])
        self.right_column_frame.setMaximumWidth(self.settings["right_column_size"]["minimum"])

        # IMPORT RIGHT COLUMN
        # ///////////////////////////////////////////////////////////////
        self.content_area_right_layout = qtw.QVBoxLayout()
        self.content_area_right_layout.setContentsMargins(5, 5, 5, 5)
        self.content_area_right_layout.setSpacing(0)
        self.right_column_frame.setLayout(self.content_area_right_layout)

        # RIGHT BG
        self.content_area_right_bg_frame = qtw.QFrame()
        self.content_area_right_bg_frame.setObjectName("content_area_right_bg_frame")
        self.content_area_right_bg_frame.setStyleSheet(
            f"""
        #content_area_right_bg_frame {{
            border-radius: 8px;
            background-color: {self.themes["app_color"]["bg_two"]};
        }}
        """
        )
        self.content_area_right_layout.addWidget(self.content_area_right_bg_frame)

        # ADD RIGHT PAGES TO RIGHT COLUMN
        self.right_column = Ui_RightColumn()
        self.right_column.setupUi(self.content_area_right_bg_frame)

        # ADD TO LAYOUTS
        self.content_area_layout.addWidget(self.right_column_frame)
        # endregion: content
        ########################################

        ########################################
        # region: credits
        self.credits_frame = qtw.QFrame()
        self.credits_frame.setMinimumHeight(26)
        self.credits_frame.setMaximumHeight(26)

        # CREATE LAYOUT
        self.credits_layout = qtw.QVBoxLayout()
        self.credits_layout.setContentsMargins(0, 0, 0, 0)
        self.credits_frame.setLayout(self.credits_layout)

        # ADD CUSTOM WIDGET CREDITS
        self.credits = PQCreditsBar(
            bg_two=self.themes["app_color"]["bg_two"],
            copyright=self.app.organization,
            version=self.app.version,
            font_family=self.settings["font"]["family"],
            text_size=self.settings["font"]["text_size"],
            text_description_color=self.themes["app_color"]["text_description"],
        )

        #  ADD TO LAYOUT
        self.credits_layout.addWidget(self.credits)
        # endregion: credits
        ########################################

        self.right_app_layout.addWidget(self.title_bar_frame)
        self.right_app_layout.addWidget(self.content_area_frame)
        self.right_app_layout.addWidget(self.credits_frame)

        self.window.layout().addWidget(self.left_menu_frame)
        self.window.layout().addWidget(self.left_column_frame)
        self.window.layout().addWidget(self.right_app_frame)

        self.setCentralWidget(self.central_widget)

    def _get_btn_sender(self):
        if self.title_bar.sender() is not None:
            return self.title_bar.sender()
        elif self.left_menu.sender() is not None:
            return self.left_menu.sender()
        elif self.left_column.sender() is not None:
            return self.left_column.sender()

    # LEFT MENU BTN IS CLICKED
    # Run function when btn is clicked
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_clicked(self):
        btn = self._get_btn_sender()
        logger.debug(f"Button {btn.objectName()}, clicked!")

    # LEFT MENU BTN IS RELEASED
    # Run function when btn is released
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_released(self):
        # GET BT CLICKED
        btn = self._get_btn_sender()
        logger.debug(f"Button {btn.objectName()}, released!")

    def _handle_window_drag(self, drag_pos: qtc.QPoint):
        self.move(self.pos() + drag_pos)

    # def changeEvent(self, event):
    #     if event.type() == event.WindowStateChange:
    #         if self.windowState() & Qt.WindowMaximized:
    #             margin = abs(self.mapToGlobal(self.rect().topLeft()).y())
    #             self.setContentsMargins(margin, margin, margin, margin)
    #         else:
    #             self.setContentsMargins(0, 0, 0, 0)
    #
    #     return super(MainWindow, self).changeEvent(event)
