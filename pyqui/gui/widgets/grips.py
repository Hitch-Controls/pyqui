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


class PQGrips(qtw.QWidget):
    def __init__(self, parent, grip_size=10, debug_grips=True):
        super().__init__(parent=parent)
        self.window = parent
        self.grip_size = grip_size

        self.top_left_grip = qtw.QFrame(parent)
        self.top_left_grip.setObjectName(u"top_left_grip")
        if debug_grips:
            self.top_left_grip.setStyleSheet(u"background-color: #333; border: 2px solid #55FF00;")

        self.top_right_grip = qtw.QFrame(parent)
        self.top_right_grip.setObjectName(u"top_right_grip")
        if debug_grips:
            self.top_right_grip.setStyleSheet(u"background-color: #333; border: 2px solid #55FF00;")

        self.bottom_left_grip = qtw.QFrame(parent)
        self.bottom_left_grip.setObjectName(u"bottom_left_grip")
        if debug_grips:
            self.bottom_left_grip.setStyleSheet(u"background-color: #333; border: 2px solid #55FF00;")

        self.bottom_right_grip = qtw.QFrame(parent)
        self.bottom_right_grip.setObjectName(u"bottom_right_grip")
        if debug_grips:
            self.bottom_right_grip.setStyleSheet(u"background-color: #333; border: 2px solid #55FF00;")

        self.top_grip = qtw.QFrame(parent)
        self.top_grip.setObjectName(u"top_grip")
        if debug_grips:
            self.top_grip.setStyleSheet(u"background-color: rgb(85, 255, 255);")
        self.top_grip.setCursor(qtg.QCursor(qtc.Qt.SizeVerCursor))

        self.bottom_grip = qtw.QFrame(parent)
        self.bottom_grip.setObjectName(u"bottom_grip")
        self.bottom_grip.setGeometry(qtc.QRect(0, 0, 500, 10))
        if debug_grips:
            self.bottom_grip.setStyleSheet(u"background-color: rgb(85, 170, 0);")
        self.bottom_grip.setCursor(qtg.QCursor(qtc.Qt.SizeVerCursor))

        self.left_grip = qtw.QFrame(parent)
        self.left_grip.setObjectName(u"left")
        self.left_grip.setCursor(qtg.QCursor(qtc.Qt.SizeHorCursor))
        if debug_grips:
            self.left_grip.setStyleSheet(u"background-color: rgb(255, 121, 198);")

        self.right_grip = qtw.QFrame(parent)
        self.right_grip.setObjectName(u"right")
        self.right_grip.setCursor(qtg.QCursor(qtc.Qt.SizeHorCursor))
        if debug_grips:
            self.right_grip.setStyleSheet(u"background-color: rgb(255, 0, 127);")

        self.resize(self.window.size())

        # grip = qtw.QSizeGrip(self.wi.top_left_grip)
        # grip.setFixedSize(self.wi.top_left_grip.size())
        # self.setGeometry(5, 5, 15, 15)

        # ENABLE COLOR

        # # SHOW TOP RIGHT GRIP
        # # ///////////////////////////////////////////////////////////////
        # if position == "top_right":
        #     self.wi.top_right(self)
        #     grip = qtw.QSizeGrip(self.wi.top_right_grip)
        #     grip.setFixedSize(self.wi.top_right_grip.size())
        #     self.setGeometry(self.parent().width() - 20, 5, 15, 15)
        #
        #     # ENABLE COLOR
        #     if disable_color:
        #         self.wi.top_right_grip.setStyleSheet("background: transparent")
        #
        # # SHOW BOTTOM LEFT GRIP
        # # ///////////////////////////////////////////////////////////////
        # if position == "bottom_left":
        #     self.wi.bottom_left(self)
        #     grip = qtw.QSizeGrip(self.wi.bottom_left_grip)
        #     grip.setFixedSize(self.wi.bottom_left_grip.size())
        #     self.setGeometry(5, self.parent().height() - 20, 15, 15)
        #
        #     # ENABLE COLOR
        #     if disable_color:
        #         self.wi.bottom_left_grip.setStyleSheet("background: transparent")
        #
        # # SHOW BOTTOM RIGHT GRIP
        # # ///////////////////////////////////////////////////////////////
        # if position == "bottom_right":
        #     self.wi.bottom_right(self)
        #     grip = qtw.QSizeGrip(self.wi.bottom_right_grip)
        #     grip.setFixedSize(self.wi.bottom_right_grip.size())
        #     self.setGeometry(self.parent().width() - 20, self.parent().height() - 20, 15, 15)
        #
        #     # ENABLE COLOR
        #     if disable_color:
        #         self.wi.bottom_right_grip.setStyleSheet("background: transparent")
        #
        # # SHOW TOP GRIP
        # # ///////////////////////////////////////////////////////////////
        # if position == "top":
        #     self.wi.top(self)
        #     self.setGeometry(0, 5, self.parent().width(), 10)
        #     self.setMaximumHeight(10)
        #
        #     # RESIZE TOP
        #     def resize_top(event):
        #         delta = event.pos()
        #         height = max(self.parent().minimumHeight(), self.parent().height() - delta.y())
        #         geo = self.parent().geometry()
        #         geo.setTop(geo.bottom() - height)
        #         self.parent().setGeometry(geo)
        #         event.accept()
        #
        #     self.wi.top_grip.mouseMoveEvent = resize_top
        #
        #     # ENABLE COLOR
        #     if disable_color:
        #         self.wi.top_grip.setStyleSheet("background: transparent")
        #
        # # SHOW BOTTOM GRIP
        # # ///////////////////////////////////////////////////////////////
        # elif position == "bottom":
        #     self.wi.bottom(self)
        #     self.setGeometry(0, self.parent().height() - 10, self.parent().width(), 10)
        #     self.setMaximumHeight(10)
        #
        #     # RESIZE BOTTOM
        #     def resize_bottom(event):
        #         delta = event.pos()
        #         height = max(self.parent().minimumHeight(), self.parent().height() + delta.y())
        #         self.parent().resize(self.parent().width(), height)
        #         event.accept()
        #
        #     self.wi.bottom_grip.mouseMoveEvent = resize_bottom
        #
        #     # ENABLE COLOR
        #     if disable_color:
        #         self.wi.bottom_grip.setStyleSheet("background: transparent")
        #
        # # SHOW LEFT GRIP
        # # ///////////////////////////////////////////////////////////////
        # elif position == "left":
        #     self.wi.left(self)
        #     self.setGeometry(0, 10, 10, self.parent().height())
        #     self.setMaximumWidth(10)
        #
        #     # RESIZE LEFT
        #     def resize_left(event):
        #         delta = event.pos()
        #         width = max(self.parent().minimumWidth(), self.parent().width() - delta.x())
        #         geo = self.parent().geometry()
        #         geo.setLeft(geo.right() - width)
        #         self.parent().setGeometry(geo)
        #         event.accept()
        #
        #     self.wi.left_grip.mouseMoveEvent = resize_left
        #
        #     # ENABLE COLOR
        #     if disable_color:
        #         self.wi.left_grip.setStyleSheet("background: transparent")
        #
        # # RESIZE RIGHT
        # # ///////////////////////////////////////////////////////////////
        # elif position == "right":
        #     self.wi.right(self)
        #     self.setGeometry(self.parent().width() - 10, 10, 10, self.parent().height())
        #     self.setMaximumWidth(10)
        #
        #     def resize_right(event):
        #         delta = event.pos()
        #         width = max(self.parent().minimumWidth(), self.parent().width() + delta.x())
        #         self.parent().resize(width, self.parent().height())
        #         event.accept()
        #
        #     self.wi.right_grip.mouseMoveEvent = resize_right
        #
        #     # ENABLE COLOR
        #     if disable_color:
        #         self.wi.right_grip.setStyleSheet("background: transparent")
        #

    # MOUSE RELEASE
    # ///////////////////////////////////////////////////////////////
    def mouseReleaseEvent(self, event):
        self.mousePos = None

    # RESIZE EVENT
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        self.top_left_grip.setGeometry(0, 0, self.grip_size, self.grip_size)
        self.top_grip.setGeometry(self.grip_size, 0, self.window.width() - self.grip_size, self.grip_size)
        self.top_right_grip.setGeometry(self.window.width() - self.grip_size, 0, self.grip_size, self.grip_size)
        self.right_grip.setGeometry(
            self.window.width() - self.grip_size, self.grip_size,
            self.grip_size, self.window.height() - self.grip_size * 2
        )
        self.bottom_right_grip.setGeometry(
            self.window.width() - self.grip_size, self.window.height() - self.grip_size * 2,
            self.grip_size, self.grip_size
        )
        self.bottom_grip.setGeometry(
            self.grip_size, self.window.height() - self.grip_size, self.window.width() - self.grip_size, self.grip_size
        )
        self.bottom_left_grip.setGeometry(0, self.window.height() - self.grip_size * 2, self.grip_size, self.grip_size)
        self.left_grip.setGeometry(0, self.grip_size, self.grip_size, self.window.height() - self.grip_size * 2)
