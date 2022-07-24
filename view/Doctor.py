from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTableWidgetItem

from model.AssignmentCount import AssignmentCount


class DoctorRows(object):

    header = ["姓名", "是否排班", "节前工作日", "工作日", "工作日系数", "无休节假日", "节假日", "节假日系数"]

    def __init__(self, doctors: list[(AssignmentCount, bool)]):
        self._data = doctors

    @property
    def rows(self) -> list[list[QTableWidgetItem]]:
        _rows: list[list[QTableWidgetItem]] = []
        for doctor in self._data:
            _rows.append(DoctorRow(doctor[0], doctor[1]).items)
        return _rows


class DoctorRow(object):

    def __init__(self, data: AssignmentCount, schedule: bool):
        self._data: AssignmentCount = data
        self._schedule: bool = schedule

    @property
    def items(self) -> list[QTableWidgetItem]:
        last_workday = self._data.last_workday
        workday = self._data.last_workday + self._data.normal_workday
        workday_index = last_workday / workday if workday != 0 else -1
        normal_holiday = self._data.normal_holiday
        holiday = self._data.last_holiday + self._data.normal_holiday
        holiday_index = normal_holiday / holiday if workday != 0 else -1
        _items: list[QTableWidgetItem] = []
        _items.append(QTableWidgetItem(self._data.name))
        _items.append(QTableWidgetItem("是" if self._schedule else "否"))
        _items.append(QTableWidgetItem(str(last_workday)))
        _items.append(QTableWidgetItem(str(workday)))
        _items.append(QTableWidgetItem(str(workday_index) if workday != 0 else "N/A"))
        _items.append(QTableWidgetItem(str(normal_holiday)))
        _items.append(QTableWidgetItem(str(holiday)))
        _items.append(QTableWidgetItem(str(holiday_index) if holiday != 0 else "N/A"))
        for _item in _items:
            _item.setFlags(_item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        return _items
