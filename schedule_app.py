import sys
from PyQt5 import QtWidgets as qw


class ScheduleWindow(qw.QMainWindow):

    def __init__(self):
        super(ScheduleWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("排班app")
        self.resize(1440, 720)
        self._calendar = qw.QCalendarWidget(self)
        self._calendar.resize(1120, 720)


if __name__ == "__main__":
    app = qw.QApplication(sys.argv)
    window = ScheduleWindow()
    window.show()
    sys.exit(app.exec_())
