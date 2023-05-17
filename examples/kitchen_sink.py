import sys

from pyqui.qt import *
from pyqui import PQApplication
from pyqui.gui.widgets import *
from pyqui.conf import get_settings
from pyqui.gui.main_window import PQMainWindow
from pyqui.resources.utils import svg_icon, svg_image

LI_TEXT = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""


class Page1(qtw.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName(u"page_1")
        self.setStyleSheet(u"font-size: 14pt")
        layout = qtw.QVBoxLayout(self)
        layout.setSpacing(5)
        layout.setObjectName(u"page_1_layout")
        layout.setContentsMargins(5, 5, 5, 5)
        self.welcome_base = qtw.QFrame(self)
        self.welcome_base.setObjectName(u"welcome_base")
        self.welcome_base.setMinimumSize(qtc.QSize(300, 150))
        self.welcome_base.setMaximumSize(qtc.QSize(300, 150))
        self.welcome_base.setFrameShape(qtw.QFrame.NoFrame)
        self.welcome_base.setFrameShadow(qtw.QFrame.Raised)
        self.center_page_layout = qtw.QVBoxLayout(self.welcome_base)
        self.center_page_layout.setSpacing(10)
        self.center_page_layout.setObjectName(u"center_page_layout")
        self.center_page_layout.setContentsMargins(0, 0, 0, 0)
        self.logo = qtw.QFrame(self.welcome_base)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(qtc.QSize(300, 120))
        self.logo.setMaximumSize(qtc.QSize(300, 120))
        self.logo.setFrameShape(qtw.QFrame.NoFrame)
        self.logo.setFrameShadow(qtw.QFrame.Raised)
        self.logo_layout = qtw.QVBoxLayout(self.logo)
        self.logo_layout.setSpacing(0)
        self.logo_layout.setObjectName(u"logo_layout")
        self.logo_layout.setContentsMargins(0, 0, 0, 0)
        self.logo_svg = QtSvgWidgets.QSvgWidget(svg_image("logo_home.svg"))
        self.logo_layout.addWidget(self.logo_svg, qtc.Qt.AlignCenter, qtc.Qt.AlignCenter)

        self.center_page_layout.addWidget(self.logo)

        self.label = qtw.QLabel(self.welcome_base)
        self.label.setObjectName(u"label")
        self.label.setAlignment(qtc.Qt.AlignCenter)
        self.label.setText("Welcome to PyQui GUI")
        self.center_page_layout.addWidget(self.label)

        layout.addWidget(self.welcome_base, 0, qtc.Qt.AlignHCenter)


class Page2(qtw.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName(u"page_2")
        self.page_2_layout = qtw.QVBoxLayout(self)
        self.page_2_layout.setSpacing(5)
        self.page_2_layout.setObjectName(u"page_2_layout")
        self.page_2_layout.setContentsMargins(5, 5, 5, 5)
        self.scroll_area = qtw.QScrollArea(self)
        self.scroll_area.setObjectName(u"scroll_area")
        # self.scroll_area.setStyleSheet(u"background: transparent;")
        self.scroll_area.setFrameShape(qtw.QFrame.NoFrame)
        self.scroll_area.setVerticalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.scroll_area.setHorizontalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        self.contents = qtw.QWidget()
        self.contents.setObjectName(u"contents")
        self.contents.setGeometry(qtc.QRect(0, 0, 840, 580))
        # self.contents.setStyleSheet(u"background: transparent;")
        self.verticalLayout = qtw.QVBoxLayout(self.contents)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.title_label = qtw.QLabel(self.contents)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setText("Custom Widgets Page")
        self.title_label.setMaximumSize(qtc.QSize(16777215, 40))
        font = qtg.QFont()
        font.setPointSize(16)
        self.title_label.setFont(font)
        # self.title_label.setStyleSheet(u"font-size: 16pt")
        self.title_label.setAlignment(qtc.Qt.AlignCenter)

        self.verticalLayout.addWidget(self.title_label)

        self.description_label = qtw.QLabel(self.contents)
        self.description_label.setText(
            u"Here will be all the custom widgets, they will be added over time on this page.\n"
            "I will try to always record a new tutorial when adding a new Widget and updating the project on Patreon before launching on GitHub and GitHub after the public release.")
        self.description_label.setObjectName(u"description_label")
        self.description_label.setAlignment(qtc.Qt.AlignHCenter | qtc.Qt.AlignTop)
        self.description_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.description_label)

        self.row_1_layout = qtw.QHBoxLayout()
        self.row_1_layout.setObjectName(u"row_1_layout")
        self.verticalLayout.addLayout(self.row_1_layout)

        self.row_2_layout = qtw.QHBoxLayout()
        self.row_2_layout.setObjectName(u"row_2_layout")
        self.verticalLayout.addLayout(self.row_2_layout)

        self.row_3_layout = qtw.QHBoxLayout()
        self.row_3_layout.setObjectName(u"row_3_layout")
        self.verticalLayout.addLayout(self.row_3_layout)

        self.row_4_layout = qtw.QVBoxLayout()
        self.row_4_layout.setObjectName(u"row_4_layout")
        self.verticalLayout.addLayout(self.row_4_layout)

        self.row_5_layout = qtw.QVBoxLayout()
        self.row_5_layout.setObjectName(u"row_5_layout")
        self.verticalLayout.addLayout(self.row_5_layout)

        self.row_6_layout = qtw.QVBoxLayout()
        self.row_6_layout.setObjectName(u"row_6_layout")
        self.verticalLayout.addLayout(self.row_6_layout)

        self.scroll_area.setWidget(self.contents)

        self.page_2_layout.addWidget(self.scroll_area)

        self._setup_widgets()

    def _setup_widgets(self):
        self.themes = get_settings().theme

        self.circular_progress_1 = PQCircularProgress(
            value=80,
            progress_color=self.themes["app_color"]["context_color"],
            text_color=self.themes["app_color"]["text_title"],
            font_size=14,
            bg_color=self.themes["app_color"]["dark_four"],
        )
        self.circular_progress_1.setFixedSize(200, 200)

        # CIRCULAR PROGRESS 2
        self.circular_progress_2 = PQCircularProgress(
            value=45,
            progress_width=4,
            progress_color=self.themes["app_color"]["green"],
            text_color=self.themes["app_color"]["green"],
            font_size=14,
            bg_color=self.themes["app_color"]["bg_three"],
        )
        self.circular_progress_2.setFixedSize(160, 160)

        # CIRCULAR PROGRESS 3
        self.circular_progress_3 = PQCircularProgress(
            value=75,
            progress_width=2,
            progress_color=self.themes["app_color"]["pink"],
            text_color=self.themes["app_color"]["white"],
            font_size=14,
            bg_color=self.themes["app_color"]["bg_three"],
        )
        self.circular_progress_3.setFixedSize(140, 140)

        # PY SLIDER 1
        self.vertical_slider_1 = PQSlider(
            margin=8,
            bg_size=10,
            bg_radius=5,
            handle_margin=-3,
            handle_size=16,
            handle_radius=8,
            bg_color=self.themes["app_color"]["dark_three"],
            bg_color_hover=self.themes["app_color"]["dark_four"],
            handle_color=self.themes["app_color"]["context_color"],
            handle_color_hover=self.themes["app_color"]["context_hover"],
            handle_color_pressed=self.themes["app_color"]["context_pressed"],
        )
        self.vertical_slider_1.setMinimumHeight(100)

        # PY SLIDER 2
        self.vertical_slider_2 = PQSlider(
            bg_color=self.themes["app_color"]["dark_three"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            handle_color=self.themes["app_color"]["context_color"],
            handle_color_hover=self.themes["app_color"]["context_hover"],
            handle_color_pressed=self.themes["app_color"]["context_pressed"],
        )
        self.vertical_slider_2.setValue(self.circular_progress_1.value)
        self.vertical_slider_2.valueChanged.connect(self.circular_progress_1.set_value)
        self.vertical_slider_2.setMinimumHeight(100)

        # PY SLIDER 3
        self.vertical_slider_3 = PQSlider(
            margin=8,
            bg_size=10,
            bg_radius=5,
            handle_margin=-3,
            handle_size=16,
            handle_radius=8,
            bg_color=self.themes["app_color"]["dark_three"],
            bg_color_hover=self.themes["app_color"]["dark_four"],
            handle_color=self.themes["app_color"]["green"],
            handle_color_hover=self.themes["app_color"]["context_hover"],
            handle_color_pressed=self.themes["app_color"]["context_pressed"],
        )
        self.vertical_slider_3.setValue(self.circular_progress_2.value)
        self.vertical_slider_3.valueChanged.connect(self.circular_progress_2.set_value)
        self.vertical_slider_3.setOrientation(qtc.Qt.Horizontal)
        self.vertical_slider_3.setMaximumWidth(200)

        # PY SLIDER 4
        self.vertical_slider_4 = PQSlider(
            bg_color=self.themes["app_color"]["dark_three"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            handle_color=self.themes["app_color"]["pink"],
            handle_color_hover=self.themes["app_color"]["context_hover"],
            handle_color_pressed=self.themes["app_color"]["context_pressed"],
        )
        self.vertical_slider_4.setValue(self.circular_progress_3.value)
        self.vertical_slider_4.valueChanged.connect(self.circular_progress_3.set_value)
        self.vertical_slider_4.setOrientation(qtc.Qt.Horizontal)
        self.vertical_slider_4.setMaximumWidth(200)

        # ICON BUTTON 1
        self.icon_button_1 = PQIconButton(
            icon_path=svg_icon("icon_heart.svg"),
            parent=self,
            app_parent=self.parent(),
            tooltip_text="Icon button - Heart",
            width=40,
            height=40,
            radius=20,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["icon_active"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["pink"],
        )

        # ICON BUTTON 2
        self.icon_button_2 = PQIconButton(
            icon_path=svg_icon("icon_add_user.svg"),
            parent=self,
            app_parent=self.parent(),
            tooltip_text="BTN with tooltip",
            width=40,
            height=40,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["green"],
        )

        # ICON BUTTON 3
        self.icon_button_3 = PQIconButton(
            icon_path=svg_icon("icon_add_user.svg"),
            parent=self,
            app_parent=self.parent(),
            tooltip_text="BTN actived! (is_actived = True)",
            width=40,
            height=40,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["context_color"],
            is_active=True,
        )

        # PUSH BUTTON 1
        self.push_button_1 = PQPushButton("Button Without Icon")
        self.push_button_1.setMinimumHeight(40)
        self.push_button_1.clicked.connect(lambda: print('btn 1 clicked'))

        # PUSH BUTTON 2
        self.push_button_2 = PQPushButton("Button With Icon")
        self.icon_2 = qtg.QIcon(svg_icon("icon_settings.svg"))
        self.push_button_2.setMinimumHeight(40)
        self.push_button_2.setIcon(self.icon_2)
        self.push_button_2.clicked.connect(lambda: print('btn 2 clicked'))

        # PY LINE EDIT
        self.line_edit = PQLineEdit(text="", place_holder_text="Place holder text")
        self.line_edit.setMinimumHeight(30)

        # Collapseable Widget
        self.collapseable_widget = CollapsableWidget("Collapaseable Section")
        li_label = qtw.QLabel(LI_TEXT)
        li_label.setWordWrap(True)
        self.collapseable_widget.addWidget(li_label)

        # TOGGLE BUTTON
        self.toggle_button = PQToggle(
            width=50,
            bg_color=self.themes["app_color"]["dark_two"],
            circle_color=self.themes["app_color"]["icon_color"],
            active_color=self.themes["app_color"]["context_color"],
        )

        # TABLE WIDGETS
        self.table_widget = qtw.QTableWidget()
        self.table_widget.setColumnCount(3)
        self.table_widget.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.Stretch)
        self.table_widget.setSelectionMode(qtw.QAbstractItemView.ExtendedSelection)
        self.table_widget.setSelectionBehavior(qtw.QAbstractItemView.SelectRows)

        # Columns / Header
        self.column_1 = qtw.QTableWidgetItem()
        self.column_1.setTextAlignment(qtc.Qt.AlignCenter)
        self.column_1.setText("COLUMN 1")

        self.column_2 = qtw.QTableWidgetItem()
        self.column_2.setTextAlignment(qtc.Qt.AlignCenter)
        self.column_2.setText("COLUMN 2")

        self.column_3 = qtw.QTableWidgetItem()
        self.column_3.setTextAlignment(qtc.Qt.AlignCenter)
        self.column_3.setText("COLUMN 3")

        # Set column
        self.table_widget.setHorizontalHeaderItem(0, self.column_1)
        self.table_widget.setHorizontalHeaderItem(1, self.column_2)
        self.table_widget.setHorizontalHeaderItem(2, self.column_3)

        for x in range(10):
            row_number = self.table_widget.rowCount()
            self.table_widget.insertRow(row_number)  # Insert row
            self.table_widget.setItem(row_number, 0, qtw.QTableWidgetItem("PyQui"))
            self.table_widget.setItem(row_number, 1, qtw.QTableWidgetItem("Qt + Python = ❤"))
            col3 = qtw.QTableWidgetItem(f'{x}')
            col3.setTextAlignment(qtc.Qt.AlignCenter)
            self.table_widget.setItem(row_number, 2, col3)  # Add pass
            self.table_widget.setRowHeight(row_number, 22)

        # ADD WIDGETS
        self.row_1_layout.addWidget(self.circular_progress_1)
        self.row_1_layout.addWidget(self.circular_progress_2)
        self.row_1_layout.addWidget(self.circular_progress_3)
        self.row_2_layout.addWidget(self.vertical_slider_1)
        self.row_2_layout.addWidget(self.vertical_slider_2)
        self.row_2_layout.addWidget(self.vertical_slider_3)
        self.row_2_layout.addWidget(self.vertical_slider_4)
        self.row_3_layout.addWidget(self.icon_button_1)
        self.row_3_layout.addWidget(self.icon_button_2)
        self.row_3_layout.addWidget(self.icon_button_3)
        self.row_3_layout.addWidget(self.push_button_1)
        self.row_3_layout.addWidget(self.push_button_2)
        self.row_3_layout.addWidget(self.toggle_button)
        self.row_4_layout.addWidget(self.line_edit)
        self.row_5_layout.addWidget(self.collapseable_widget)
        self.row_6_layout.addWidget(self.table_widget)


class Page3(qtw.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName(u"page_3")
        self.page_3_layout = PQBorderLayout(self)
        self.page_3_layout.setObjectName(u"page_3_layout")

        font = qtg.QFont()
        font.setPointSize(16)
        for i, j in enumerate(range(8)):
            label = qtw.QLabel(self)
            label.setText(f'Position: {PQBorderLayout.BorderPosition(i % 4).name} [{j}]')
            label.setFont(font)
            label.setAlignment(qtc.Qt.AlignCenter)
            label.setStyleSheet("background: #21252d; font-size: 16px; padding: 10px;")
            self.page_3_layout.addWidget(label, PQBorderLayout.BorderPosition(i % 4))

        center_widget = qtw.QWidget(self)
        center_widget_layout = qtw.QVBoxLayout(center_widget)
        label = qtw.QLabel(self)
        label.setText('Extra Layouts!\nThis is a DSBorderLayout with a DSFlowLayout in the center.\n\n')
        label.setWordWrap(True)
        label.setStyleSheet("font-size: 24px;")
        label.setAlignment(qtc.Qt.AlignCenter)
        center_widget_layout.addWidget(label)

        flow_widget = qtw.QWidget(self)
        flow_layout = PQFlowLayout(flow_widget)
        for i in range(10):
            flow_layout.addWidget(qtw.QPushButton("Short"))
            flow_layout.addWidget(qtw.QPushButton("Longer"))
            flow_layout.addWidget(qtw.QPushButton("Different text"))
            flow_layout.addWidget(qtw.QPushButton("More text"))
            flow_layout.addWidget(qtw.QPushButton("Even longer button text"))
        center_widget_layout.addWidget(flow_widget, PQBorderLayout.Center)
        self.page_3_layout.addWidget(center_widget, PQBorderLayout.Center)


class MyMainWindow(PQMainWindow):
    add_left_menus = [
        {
            "btn_icon": "icon_home.svg",
            "btn_id": "btn_home",
            "btn_text": "Home",
            "btn_tooltip": "Home page",
            "show_top": True,
            "is_active": True,
        },
        {
            "btn_icon": "icon_widgets.svg",
            "btn_id": "btn_widgets",
            "btn_text": "Show Custom Widgets",
            "btn_tooltip": "Show custom widgets",
            "show_top": True,
            "is_active": False,
        },
        {
            "btn_icon": "icon_add_user.svg",
            "btn_id": "btn_add_user",
            "btn_text": "Add Users",
            "btn_tooltip": "Add users",
            "show_top": True,
            "is_active": False,
        },
        {
            "btn_icon": "icon_file.svg",
            "btn_id": "btn_new_file",
            "btn_text": "New File",
            "btn_tooltip": "Create new file",
            "show_top": True,
            "is_active": False,
        },
        {
            "btn_icon": "icon_folder_open.svg",
            "btn_id": "btn_open_file",
            "btn_text": "Open File",
            "btn_tooltip": "Open file",
            "show_top": True,
            "is_active": False,
        },
        {
            "btn_icon": "icon_save.svg",
            "btn_id": "btn_save",
            "btn_text": "Save File",
            "btn_tooltip": "Save file",
            "show_top": True,
            "is_active": False,
        },
        {
            "btn_icon": "icon_info.svg",
            "btn_id": "btn_info",
            "btn_text": "Information",
            "btn_tooltip": "Open informations",
            "show_top": False,
            "is_active": False,
        },
        {
            "btn_icon": "icon_settings.svg",
            "btn_id": "btn_settings",
            "btn_text": "Settings",
            "btn_tooltip": "Open settings",
            "show_top": False,
            "is_active": False,
        },
    ]

    add_title_bar_menus = [
        {"btn_icon": "icon_search.svg", "btn_id": "btn_search", "btn_tooltip": "Search", "is_active": False},
        {
            "btn_icon": "icon_settings.svg",
            "btn_id": "btn_top_settings",
            "btn_tooltip": "Top settings",
            "is_active": False,
        },
    ]

    def _init_widgets(self):
        super()._init_widgets()

        self.page_1 = Page1(self.central_widget)
        self.stacked_pages.addWidget(self.page_1)

        self.page_2 = Page2(self.central_widget)
        self.stacked_pages.addWidget(self.page_2)

        self.page_3 = Page3(self.central_widget)
        self.stacked_pages.addWidget(self.page_3)

        self.left_menu.add_menus(self.add_left_menus)
        self.title_bar.add_menus(self.add_title_bar_menus)

        # # SET INITIAL PAGE / SET LEFT AND RIGHT COLUMN MENUS
        # # ///////////////////////////////////////////////////////////////
        self.set_page(self.page_1)
        self.set_left_column_menu(
            menu=self.left_column.menus.menu_1,
            title="Settings Left Column",
            icon_path=svg_icon("icon_settings.svg"),
        )
        self.set_right_column_menu(self.right_column.menu_1)

        self._init_columns()

    def _init_columns(self):
        # RIGHT COLUMN
        # ///////////////////////////////////////////////////////////////

        # BTN 1
        self.right_btn_1 = PQPushButton("Show Menu 2")
        self.icon_right = qtg.QIcon(svg_icon("icon_arrow_right.svg"))
        self.right_btn_1.setIcon(self.icon_right)
        self.right_btn_1.setMaximumHeight(40)
        self.right_btn_1.clicked.connect(lambda: self.set_right_column_menu(
            self.right_column.menu_2
        ))
        self.right_column.btn_1_layout.addWidget(self.right_btn_1)

        # BTN 2
        self.right_btn_2 = PQPushButton("Show Menu 1")
        self.icon_left = qtg.QIcon(svg_icon("icon_arrow_left.svg"))
        self.right_btn_2.setIcon(self.icon_left)
        self.right_btn_2.setMaximumHeight(40)
        self.right_btn_2.clicked.connect(lambda: self.set_right_column_menu(
            self.right_column.menu_1
        ))
        self.right_column.btn_2_layout.addWidget(self.right_btn_2)

        # ///////////////////////////////////////////////////////////////
        # END - EXAMPLE CUSTOM WIDGETS
        # ///////////////////////////////////////////////////////////////

    def btn_clicked(self):
        btn = self._get_btn_sender()

        # Remove Selection If Clicked By "btn_close_left_column"
        # if btn.objectName() != "btn_settings":
        #     self.left_menu.deselect_all_tab()

        # top_settings = self.get_title_bar_btn(self, "btn_top_settings")
        # top_settings.set_active(False)

        # LEFT MENU
        # ///////////////////////////////////////////////////////////////
        # HOME BTN
        if btn.objectName() == "btn_home":
            # Select Menu
            self.left_menu.select_only_one(btn.objectName())

            # Load Page 1
            self.set_page(self.page_1)

        # WIDGETS BTN
        if btn.objectName() == "btn_widgets":
            # Select Menu
            self.left_menu.select_only_one(btn.objectName())

            # Load Page 2
            self.set_page(self.page_2)

        # LOAD USER PAGE
        if btn.objectName() == "btn_add_user":
            # Select Menu
            self.left_menu.select_only_one(btn.objectName())

            self.set_page(self.page_3)

        # BOTTOM INFORMATION
        if btn.objectName() == "btn_info":
            # CHECK IF LEFT COLUMN IS VISIBLE
            if not self.left_column_is_visible():
                self.left_menu.select_only_one_tab(btn.objectName())

                # Show / Hide
                self.toggle_left_column()
                self.left_menu.select_only_one_tab(btn.objectName())
            else:
                if btn.objectName() == "btn_close_left_column":
                    self.left_menu.deselect_all_tab()
                    # Show / Hide
                    self.toggle_left_column()
                self.left_menu.select_only_one_tab(btn.objectName())

            # Change Left Column Menu
            if btn.objectName() != "btn_close_left_column":
                self.set_left_column_menu(
                    menu=self.left_column.menus.menu_2,
                    title="Info tab",
                    icon_path=svg_icon("icon_info.svg"),
                )

        # SETTINGS LEFT
        if btn.objectName() == "btn_settings" or btn.objectName() == "btn_close_left_column":
            # CHECK IF LEFT COLUMN IS VISIBLE
            if not self.left_column_is_visible():
                # Show / Hide
                self.toggle_left_column()
                self.left_menu.select_only_one_tab(btn.objectName())
            else:
                if btn.objectName() == "btn_close_left_column":
                    self.left_menu.deselect_all_tab()
                    # Show / Hide
                    self.toggle_left_column()
                self.left_menu.select_only_one_tab(btn.objectName())

            # Change Left Column Menu
            if btn.objectName() != "btn_close_left_column":
                self.set_left_column_menu(
                    menu=self.left_column.menus.menu_1,
                    title="Settings Left Column",
                    icon_path=svg_icon("icon_settings.svg"),
                )
        # TITLE BAR MENU
        # ///////////////////////////////////////////////////////////////
        # SETTINGS TITLE BAR
        if btn.objectName() == "btn_top_settings":
            # Toogle Active
            if not self.right_column_is_visible():
                btn.set_active(True)

                # Show / Hide
                self.toggle_right_column()
            else:
                btn.set_active(False)

                # Show / Hide
                self.toggle_right_column()

            top_settings = self.get_left_menu_btn("btn_settings")
            # top_settings.set_active_tab(False)


if __name__ == "__main__":
    app = PQApplication(sys.argv, main_window_cls=MyMainWindow)
    sys.exit(app.exec())
