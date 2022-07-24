from PySide6.QtWidgets import QMainWindow, QWidget, QPushButton
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout

from model.assignment_count import AssignmentCount

from view.ScheduleCalendar import ScheduleCalendar
from view.DoctorList import DoctorList


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("排班程序")
        # self.setMinimumSize(1120, 540)
        # self.setMaximumSize(1920, 1080)

        self._calendar = None
        self._doctors = None
        self._central_widget = QWidget(self)
        self.setCentralWidget(self._central_widget)
        self._layout = QHBoxLayout()
        self._central_widget.setLayout(self._layout)

        self._right_widget = QWidget(self)
        self._right_widget.setLayout(QVBoxLayout())
        self._layout.addWidget(self.create_calendar())
        self._layout.addWidget(self._right_widget)
        self._right_widget.layout().addWidget(self.create_doctor_list())
        self._right_widget.layout().addWidget(QPushButton(text="OK", parent=self._right_widget))

    def create_calendar(self):
        self._calendar = ScheduleCalendar(parent=self)
        self._calendar.setMinimumSize(600, 720)
        return self._calendar

    def create_doctor_list(self):
        self._doctors = DoctorList(parent=self)
        self._doctors.setFixedWidth(820)
        data = []
        for i in range(50):
            data.append((AssignmentCount("张"+str(i)), True))
        self._doctors.set_data(data)

        return self._doctors
