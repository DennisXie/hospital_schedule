from PySide6.QtCore import Qt, QPoint, Signal, QObject, QEvent
from PySide6.QtWidgets import QTableWidget, QHeaderView, QMenu
from PySide6.QtGui import QAction

from model.AssignmentCount import AssignmentCount
from view.Doctor import DoctorRows


class DoctorList(QTableWidget):

    right_clicked = Signal()

    def __init__(self, parent):
        super(DoctorList, self).__init__(parent)
        self._data = []
        self._show()

    def set_data(self, data: list[(AssignmentCount, bool)]):
        self._data = data
        self._show()

    def _show(self):
        self.setRowCount(len(self._data))
        self.setColumnCount(len(DoctorRows.header))
        self.setHorizontalHeaderLabels(DoctorRows.header)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.setAutoScroll(True)
        self.verticalHeader().setVisible(False)
        rows = DoctorRows(self._data).rows
        for i, row in enumerate(rows):
            for j, item in enumerate(row):
                self.setItem(i, j, item)
        self.customContextMenuRequested.connect(self._show_menu)

    def cellClicked(self, *args, **kwargs):
        super(DoctorList, self).__init__(*args, **kwargs)
        self._show_menu(*args)

    def _show_menu(self, pos: QPoint):
        menu = QMenu(self)
        item = self.indexAt(pos)
        action = QAction("Action 1", self.parent())
        action.triggered.connect(self._p)
        menu.addAction(action)
        menu.addAction(QAction("Action 2", self.parent()))
        menu.popup(self.viewport().mapToGlobal(pos))

    def _p(self):
        print("abcde")
