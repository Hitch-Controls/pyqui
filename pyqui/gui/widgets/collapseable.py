from pyqui.qt import *
from pyqui.resources.utils import svg_icon


ANIM_DURATION = 100


class CollapsableWidget(qtw.QFrame):
    def __init__(self, label, expand=False, parent=None):
        super().__init__(parent=parent)
        self.label = label
        self.expanded = False
        self.expanded_icon = qtg.QIcon(svg_icon("icon_arrow_down.svg")).pixmap(10, 10)
        self.collapsed_icon = qtg.QIcon(svg_icon("icon_arrow_right.svg")).pixmap(10, 10)

        self.main_layout = qtw.QVBoxLayout(self)
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.header_icon = qtg.QIcon(svg_icon("icon_arrow_right.svg")).pixmap(10, 10)
        self.header = qtw.QPushButton(label)
        self.header.setObjectName("CollapsableHeader")
        self.header.setStyleSheet(
            "text-align: left; padding-left: 5px; border-radius: 0px; background: transparent;"
        )
        self.header.setIcon(self.header_icon)

        self.content_widget = qtw.QWidget()
        self.content_widget.setObjectName('CollapsableContent')
        self.content_layout = qtw.QVBoxLayout(self.content_widget)
        self.content_layout.setSpacing(0)
        self.content_layout.setContentsMargins(5, 5, 5, 5)
        self.main_layout.addWidget(self.header, 0, qtc.Qt.AlignTop)
        self.main_layout.addWidget(self.content_widget, 0, qtc.Qt.AlignTop)
        self.header.clicked.connect(self.toggle)

        self._animation = qtc.QVariantAnimation(self)
        self._animation.setStartValue(0)
        self._animation.setEndValue(90)
        self._animation.setDuration(ANIM_DURATION)
        self._animation.setEasingCurve(qtc.QEasingCurve.InOutCubic)
        self._animation.valueChanged.connect(self._update_animation)

        if expand:
            self.expand(0)
        else:
            self.collapse()

    def _update_animation(self, value):
        t = qtg.QTransform()
        t.rotate(value)
        p = self.header_icon.transformed(t)
        p = p.scaledToWidth(self.header_icon.size().width())
        self.header.setIcon(p)

    def addWidget(self, widget):
        self.content_layout.addWidget(widget)

    def _start_animation(self, end_value, anim_duration):
        self._animation.stop()
        self._animation.setStartValue(self._animation.currentValue())
        self._animation.setEndValue(end_value)
        self._animation.setDuration(anim_duration)
        self._animation.start()

    def collapse(self, anim_duration=ANIM_DURATION):
        self.content_widget.hide()
        # self.header.setIcon(self.collapsed_icon)
        self._start_animation(0, anim_duration)
        self.expanded = False

    def expand(self, anim_duration=ANIM_DURATION):
        self.content_widget.show()
        # self.header.setIcon(self.expanded_icon)
        self._start_animation(90, anim_duration)
        self.expanded = True

    def toggle(self):
        if self.expanded:
            self.collapse()
        else:
            self.expand()
