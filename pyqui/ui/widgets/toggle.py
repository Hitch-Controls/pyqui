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


class PQToggle(qtw.QCheckBox):
    def __init__(
            self,
            starting_state=qtc.Qt.Unchecked,
            width=50,
            bg_color="#777",
            circle_color="#DDD",
            active_color="#00BCFF",
            animation_curve=qtc.QEasingCurve.OutBounce,
            parent=None,
    ):
        super().__init__()
        self.setFixedSize(width, 28)
        self.setCursor(qtc.Qt.PointingHandCursor)
        self.setCheckState(starting_state)

        # COLORS
        self._bg_color = bg_color
        self._circle_color = circle_color
        self._active_color = active_color

        self._position = self.width() - 26 if self.isChecked() else 3
        self.animation = qtc.QPropertyAnimation(self, b"position")
        self.animation.setEasingCurve(animation_curve)
        self.animation.setDuration(500)
        self.stateChanged.connect(self.setup_animation)

    @qtc.Property(float)
    def position(self):
        return self._position

    @position.setter
    def position(self, pos):
        self._position = pos
        self.update()

    # START STOP ANIMATION
    def setup_animation(self, value):
        self.animation.stop()
        if value:
            self.animation.setEndValue(self.width() - 26)
        else:
            self.animation.setEndValue(4)
        self.animation.start()

    def hitButton(self, pos: qtc.QPoint):
        return self.contentsRect().contains(pos)

    def paintEvent(self, e):
        p = qtg.QPainter(self)
        p.setRenderHint(qtg.QPainter.Antialiasing)
        p.setFont(qtg.QFont("Segoe UI", 9))

        # SET PEN
        p.setPen(qtc.Qt.NoPen)

        # DRAW RECT
        rect = qtc.QRect(0, 0, self.width(), self.height())

        if not self.isChecked():
            p.setBrush(qtg.QColor(self._bg_color))
            p.drawRoundedRect(0, 0, rect.width(), 28, 14, 14)
            p.setBrush(qtg.QColor(self._circle_color))
            p.drawEllipse(self._position, 3, 22, 22)
        else:
            p.setBrush(qtg.QColor(self._active_color))
            p.drawRoundedRect(0, 0, rect.width(), 28, 14, 14)
            p.setBrush(qtg.QColor(self._circle_color))
            p.drawEllipse(self._position, 3, 22, 22)

        p.end()
