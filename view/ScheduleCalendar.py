from PySide6.QtCore import Qt, QRect, QDate, QPoint
from PySide6.QtGui import QPainter, QFont, QColor, QAction
from PySide6.QtWidgets import QCalendarWidget, QMenu

from model.assignment import Assignment


class ScheduleCalendar(QCalendarWidget):
    def __init__(self, parent=None):
        super(ScheduleCalendar, self).__init__(parent)
        self._data: dict[str, Assignment] = {}
        self._show()

    def set_data(self, assignments: list[Assignment]) -> None:
        self._data = {assignment.key: assignment for assignment in assignments}
        self._show()

    def _show(self):
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self._show_menu)

    def get_assignment(self, date: QDate) -> Assignment:
        key: str = Assignment.generate_key(date.year(), date.month(), date.day())
        return self._data.get(key)

    def paintCell(self, painter: QPainter, rect: QRect, date: QDate) -> None:
        # super(ScheduleCalendar, self).paintCell(painter, rect, date)
        assignment: Assignment = self.get_assignment(date)
        name = assignment.name if assignment else ""
        holiday = assignment.holiday if assignment else False
        ignore = assignment.ignore if assignment else False

        painter.save()
        if self.monthShown() != date.month():
            painter.setPen("#DCDCDC")
            painter.drawText(rect, Qt.AlignCenter, name)
            painter.drawText(rect, Qt.AlignTop | Qt.AlignHCenter, str(date.day()))
        elif holiday and not ignore:
            painter.drawText(rect, Qt.AlignCenter, name)
            painter.setPen("#3091c9")
            painter.drawText(rect, Qt.AlignTop | Qt.AlignHCenter, str(date.day()))
        elif holiday and ignore:
            painter.drawText(rect, Qt.AlignCenter, name)
            painter.setPen(QColor.red())
            painter.drawText(rect, Qt.AlignTop | Qt.AlignHCenter, str(date.day()))
        else:
            painter.drawText(rect, Qt.AlignCenter, name)
            painter.drawText(rect, Qt.AlignTop | Qt.AlignHCenter, str(date.day()))
        painter.restore()
        # font = painter.font()
        # pen = painter.pen()
        # bold = QFont(font.families(), 11)
        # bold.setBold(True)
        # if self.holiday(date):
        #     painter.setPen("#3091c9")
        # painter.setFont(bold)
        # painter.setFont(font)
        # painter.setPen(pen)

    def holiday(self, date: QDate) -> bool:
        return date.dayOfWeek() >= 6

    def _show_date(self, date: QDate):
        print(date.day())

       # self.activated.connect(self._show_date)
        # self.setDateEditEnabled(True)

    def _show_menu(self, pos: QPoint):
        menu = QMenu(self)
        item = self.childAt(pos)
        action = QAction("Action 1", self.parent())
        menu.addAction(action)
        menu.addAction(QAction("Action 2", self.parent()))
        menu.popup(self.mapToGlobal(pos))
        date: QDate = self.selectedDate()
        print(date.day())
