import enum
from collections import namedtuple

from pyqui.qt import *

_BorderItemWrapper = namedtuple('_BorderItemWrapper', ['item', 'position'])


class BorderPosition(enum.IntEnum):
    North = 0
    East = 1
    South = 2
    West = 3
    Center = 4


class PQBorderLayout(qtw.QLayout):
    BorderPosition = BorderPosition
    North, East, South, West, Center = [BorderPosition(_) for _ in range(5)]
    MinimumSize = 0
    SizeHint = 1

    def __init__(self, parent=None, margin=0, spacing=-1):
        super().__init__(parent)

        self.setContentsMargins(margin, margin, margin, margin)
        self.setSpacing(spacing)
        self.items = []

    def __del__(self):
        while self.takeAt(0):
            pass

    def addItem(self, item, position: BorderPosition):
        self._add(item, position)

    def addWidget(self, widget: qtw.QWidget, position: BorderPosition):
        self._add(qtw.QWidgetItem(widget), position)

    def expandingDirections(self):
        return qtc.Qt.Horizontal | qtc.Qt.Vertical

    def hasHeightForWidth(self):
        return False

    def count(self):
        return len(self.items)

    def itemAt(self, index):
        if index < len(self.items):
            return self.items[index].item
        return None

    def minimumSize(self):
        return self.calculateSize(PQBorderLayout.MinimumSize)

    def setGeometry(self, rect):
        center = None
        eastWidth = 0
        westWidth = 0
        northHeight = 0
        southHeight = 0
        centerHeight = 0

        super().setGeometry(rect)

        for wrapper in self.items:
            item = wrapper.item
            position = wrapper.position

            if position == BorderPosition.North:
                item.setGeometry(QtCore.QRect(rect.x(), northHeight,
                                              rect.width(), item.sizeHint().height()))

                northHeight += item.geometry().height() + self.spacing()

            elif position == BorderPosition.South:
                item.setGeometry(QtCore.QRect(item.geometry().x(),
                                              item.geometry().y(), rect.width(),
                                              item.sizeHint().height()))

                southHeight += item.geometry().height() + self.spacing()

                item.setGeometry(QtCore.QRect(rect.x(),
                                              rect.y() + rect.height() - southHeight + self.spacing(),
                                              item.geometry().width(), item.geometry().height()))

            elif position == BorderPosition.Center:
                center = wrapper

        centerHeight = rect.height() - northHeight - southHeight

        for wrapper in self.items:
            item = wrapper.item
            position = wrapper.position

            if position == PQBorderLayout.West:
                item.setGeometry(QtCore.QRect(rect.x() + westWidth,
                                              northHeight, item.sizeHint().width(), centerHeight))

                westWidth += item.geometry().width() + self.spacing()

            elif position == PQBorderLayout.East:
                item.setGeometry(QtCore.QRect(item.geometry().x(),
                                              item.geometry().y(), item.sizeHint().width(),
                                              centerHeight))

                eastWidth += item.geometry().width() + self.spacing()

                item.setGeometry(QtCore.QRect(rect.x() + rect.width() - eastWidth + self.spacing(),
                                              northHeight, item.geometry().width(),
                                              item.geometry().height()))

        if center:
            center.item.setGeometry(QtCore.QRect(westWidth, northHeight,
                                                 rect.width() - eastWidth - westWidth, centerHeight))

    def sizeHint(self):
        return self.calculateSize(PQBorderLayout.SizeHint)

    def takeAt(self, index):
        if 0 <= index < len(self.items):
            layout_struct = self.items.pop(index)
            return layout_struct.item
        return None

    def _add(self, item: qtw.QWidgetItem, position: BorderPosition):
        self.items.append(_BorderItemWrapper(item, position))

    def calculateSize(self, sizeType):
        totalSize = QtCore.QSize()

        for wrapper in self.items:
            position = wrapper.position

            if sizeType == PQBorderLayout.MinimumSize:
                itemSize = wrapper.item.minimumSize()
            else:  # sizeType == BorderLayout.SizeHint
                itemSize = wrapper.item.sizeHint()

            if position in (PQBorderLayout.North, PQBorderLayout.South, PQBorderLayout.Center):
                totalSize.setHeight(totalSize.height() + itemSize.height())

            if position in (PQBorderLayout.West, PQBorderLayout.East, PQBorderLayout.Center):
                totalSize.setWidth(totalSize.width() + itemSize.width())
        return totalSize


class PQFlowLayout(qtw.QLayout):
    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            self.setContentsMargins(qtc.QMargins(0, 0, 0, 0))
        self._items = []

    def __del__(self):
        while self.takeAt(0):
            pass

    def addItem(self, item):
        self._items.append(item)

    def count(self):
        return len(self._items)

    def itemAt(self, index):
        if 0 <= index < len(self._items):
            return self._items[index]
        return None

    def takeAt(self, index):
        if 0 <= index < len(self._items):
            return self._items.pop(index)
        return None

    def expandingDirections(self):
        return qtc.Qt.Orientation(0)

    def hasHeightForWidth(self):
        return True

    def heightForWidth(self, width):
        height = self._do_layout(qtc.QRect(0, 0, width, 0), True)
        return height

    def setGeometry(self, rect):
        super().setGeometry(rect)
        self._do_layout(rect, False)

    def sizeHint(self):
        return self.minimumSize()

    def minimumSize(self):
        size = qtc.QSize()

        for item in self._items:
            size = size.expandedTo(item.minimumSize())

        size += qtc.QSize(2 * self.contentsMargins().top(), 2 * self.contentsMargins().top())
        return size

    def _do_layout(self, rect, test_only):
        x = rect.x()
        y = rect.y()
        line_height = 0
        spacing = self.spacing()

        for item in self._items:
            style = item.widget().style()
            layout_spacing_x = style.layoutSpacing(
                qtw.QSizePolicy.PushButton, qtw.QSizePolicy.PushButton, qtc.Qt.Horizontal
            )
            layout_spacing_y = style.layoutSpacing(
                qtw.QSizePolicy.PushButton, qtw.QSizePolicy.PushButton, qtc.Qt.Vertical
            )
            space_x = spacing + layout_spacing_x
            space_y = spacing + layout_spacing_y
            next_x = x + item.sizeHint().width() + space_x
            if next_x - space_x > rect.right() and line_height > 0:
                x = rect.x()
                y = y + line_height + space_y
                next_x = x + item.sizeHint().width() + space_x
                line_height = 0

            if not test_only:
                item.setGeometry(qtc.QRect(qtc.QPoint(x, y), item.sizeHint()))

            x = next_x
            line_height = max(line_height, item.sizeHint().height())

        return y + line_height - rect.y()
