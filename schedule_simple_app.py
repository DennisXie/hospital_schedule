import sys
from PyQt5 import QtWidgets as qw
from schedule_core import Scheduler


class ScheduleSimpleWindow(qw.QDialog):

    def __init__(self):
        super(ScheduleSimpleWindow, self).__init__()
        self.init()

    def init(self):
        self.setWindowTitle("排班app极速版")
        self.setFixedWidth(300)
        self._calendar_input = qw.QLineEdit(self)
        self._calendar_input.setToolTip("例: 2022")
        self._calendar_create = qw.QPushButton("生成日历", self)
        self._schedule_input = qw.QLineEdit(self)
        self._schedule_input.setToolTip("例: 202202")
        self._schedule_btn = qw.QPushButton("生成排班", self)
        self._stats_btn = qw.QPushButton("统计", self)
        self._status_bar = qw.QStatusBar(self)

        self._layout = qw.QGridLayout(self)
        self._layout.addWidget(self._calendar_input, 0, 0, 1, 1)
        self._layout.addWidget(self._calendar_create, 0, 1, 1, 1)
        self._layout.addWidget(self._schedule_input, 1, 0, 1, 1)
        self._layout.addWidget(self._schedule_btn, 1, 1, 1, 1)
        self._layout.addWidget(self._stats_btn, 2, 1, 1, 1)
        self._layout.addWidget(self._status_bar, 3, 0, 1, 2)
        self._schedule_btn.clicked.connect(self.create_schedule)
        self._calendar_create.clicked.connect(self.create_calendar)
        self._stats_btn.clicked.connect(self.stats)

        self._scheduler = Scheduler(self.__print__)
        self._scheduler.check_and_create_dir()

    def create_schedule(self):
        input = self._schedule_input.text()
        ym = int(input)
        year = ym // 100
        month = ym % 100
        schedule_file, stats_file = self._scheduler.schedule_for_month(year, month)
        message = "排班文件位于: {}\n统计文件位于: {}".format(schedule_file, stats_file)
        qw.QMessageBox.information(self, "生成成功", message, qw.QMessageBox.Ok)

    def create_calendar(self):
        input = self._calendar_input.text()
        calendar = self._scheduler.generate_days(int(input))
        message = "日历文件位于: {}".format(calendar)
        qw.QMessageBox.information(self, "生成成功", message, qw.QMessageBox.Ok)

    def stats(self):
        f = self._scheduler.stats_history()
        message = "统计文件位于: {}".format(f)
        qw.QMessageBox.information(self, "统计完成", message, qw.QMessageBox.Ok)

    def __print__(self, *args):
        s = ''
        for arg in args:
            s += arg
        self._status_bar.showMessage(s)


class QLabelBuddy(qw.QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QLabel Example')
        self.setFixedWidth(250)

        nameLabel = qw.QLabel('&Name',self)
        nameLineEdit = qw.QLineEdit(self)
        nameLabel.setBuddy(nameLineEdit)

        passwordLabel = qw.QLabel('&Password',self)
        passwordLineEdit = qw.QLineEdit(self)
        passwordLabel.setBuddy(passwordLineEdit)

        btnOK = qw.QPushButton('&OK')
        btnCancel = qw.QPushButton('&Cancel')

        mainLayout = qw.QGridLayout(self)
        mainLayout.addWidget(nameLabel,0,0)
        mainLayout.addWidget(nameLineEdit,0,1,1,2)

        mainLayout.addWidget(passwordLabel,1,0)
        mainLayout.addWidget(passwordLineEdit,1,1,1,2)

        mainLayout.addWidget(btnOK,2,1)
        mainLayout.addWidget(btnCancel,2,2)


if __name__ == "__main__":
    app = qw.QApplication(sys.argv)
    # window = QLabelBuddy()
    window = ScheduleSimpleWindow()
    window.show()
    sys.exit(app.exec_())
