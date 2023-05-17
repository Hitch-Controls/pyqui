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


class PQTableWidget(qtw.QTableWidget):
    pass


class PQTableDraggableRowsWidget(qtw.QTableWidget):

    rowOrderChanged = qtc.Signal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.viewport().setAcceptDrops(True)
        self.setDragDropOverwriteMode(False)
        self.setDropIndicatorShown(True)

        self.setSelectionMode(qtw.QAbstractItemView.ExtendedSelection)
        self.setSelectionBehavior(qtw.QAbstractItemView.SelectRows)
        self.setDragDropMode(qtw.QAbstractItemView.InternalMove)

    def dropEvent(self, event: qtg.QDropEvent):
        if not event.isAccepted() and event.source() == self:
            drop_row = self.drop_on(event)

            rows = sorted(set(item.row() for item in self.selectedItems()))
            rows_to_move = [
                [self.takeItem(row_index, column_index) for column_index in range(self.columnCount())]
                for row_index in rows
            ]

            for row_index in reversed(rows):
                self.removeRow(row_index)
                if row_index < drop_row:
                    drop_row -= 1

            for row_index, data in enumerate(rows_to_move):
                row_index += drop_row
                self.insertRow(row_index)
                for column_index, column_data in enumerate(data):
                    if column_data is not None:
                        self.setItem(row_index, column_index, column_data)
                        column_data.setSelected(True)
            event.accept()
            self.rowOrderChanged.emit()
        super().dropEvent(event)

    def drop_on(self, event):
        index = self.indexAt(event.pos())
        if not index.isValid():
            return self.rowCount()

        return index.row() + 1 if self.is_below(event.pos(), index) else index.row()

    def is_below(self, pos, index):
        rect = self.visualRect(index)
        margin = 2
        if pos.y() - rect.top() < margin:
            return False
        elif rect.bottom() - pos.y() < margin:
            return True
        return (
            rect.contains(pos, True)
            and not (int(self.model().flags(index)) & qtc.Qt.ItemIsDropEnabled)
            and pos.y() >= rect.center().y()
        )
