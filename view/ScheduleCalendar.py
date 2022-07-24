from PySide6.QtCore import Qt, QRect, QDate
from PySide6.QtGui import QPainter, QFont, QColor
from PySide6.QtWidgets import QCalendarWidget


class ScheduleCalendar(QCalendarWidget):
    def __init__(self, parent=None):
        super(ScheduleCalendar, self).__init__(parent)

    def paintCell(self, painter: QPainter, rect: QRect, date: QDate) -> None:
        # super(ScheduleCalendar, self).paintCell(painter, rect, date)
        painter.drawText(rect, Qt.AlignCenter, "张三三")
        font = painter.font()
        pen = painter.pen()
        bold = QFont(font.families(), 11)
        bold.setBold(True)
        if date.dayOfWeek() >= 6:
            painter.setPen("#3091c9")
        painter.setFont(bold)
        painter.drawText(rect, Qt.AlignTop | Qt.AlignHCenter, str(date.day()))
        painter.setFont(font)
        painter.setPen(pen)
