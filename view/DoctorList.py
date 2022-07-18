from PySide6.QtCore import Qt, QPoint, Signal, QObject, QEvent
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QMenu
from PySide6.QtGui import QAction


class DoctorList(QTableWidget):

    right_clicked = Signal()

    def __init__(self, parent):
        super(DoctorList, self).__init__(parent)
        self.setColumnCount(2)
        self.setHorizontalHeaderLabels(["姓名", "是否值班"])
        self._doctors = ["菠萝", "香蕉", "Orange", "Apple"]
        self._show()

    def _show(self):
        self.setRowCount(len(self._doctors))
        self.setColumnCount(2)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        for i, _name in enumerate(self._doctors):
            name = QTableWidgetItem(_name)
            name.setFlags(name.flags() ^ Qt.ItemFlag.ItemIsEditable)
            duty = QTableWidgetItem("是")
            duty.setFlags(duty.flags() ^ Qt.ItemFlag.ItemIsEditable)
            self.setItem(i, 0, name)
            self.setItem(i, 1, duty)
        self.setAutoScroll(True)
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
