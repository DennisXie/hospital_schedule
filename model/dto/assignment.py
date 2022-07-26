import datetime


class Assignment(object):

    def __init__(self, date: datetime.date | str, name: str, holiday: bool = False, ignore: bool = False):
        self.date = date if isinstance(date, datetime.date) else datetime.datetime.strptime(date, "%Y-%m-%d").date()
        self.name = name
        self.holiday = holiday
        self.ignore = ignore
        self.id = None

    @property
    def key(self) -> str:
        return Assignment.generate_key(self.date.year, self.date.month, self.date.day)

    @staticmethod
    def generate_key(year: int, month: int, day: int) -> str:
        return "{}-{}-{}".format(year, month, day)
