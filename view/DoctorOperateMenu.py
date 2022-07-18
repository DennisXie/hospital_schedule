from PySide6.QtWidgets import QMenu, QTableWidget
from PySide6.QtCore import QPoint
from PySide6.QtGui import QAction


class DoctorOperateMenu(QMenu):

    def __init__(self, parent: QTableWidget):
        super(DoctorOperateMenu, self).__init__(parent)
        self.addAction(QAction("排班", parent))
        self.addAction(QAction("删除", parent))
