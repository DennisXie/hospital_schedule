class AssignmentCount(object):

    def __init__(self, name):
        self.name = name
        self.normal_workday = 0
        self.last_workday = 0
        self.normal_holiday = 0
        self.last_holiday = 0

    @property
    def total(self):
        return self.normal_holiday + self.last_holiday + self.normal_workday + self.last_workday

    @property
    def holiday(self):
        return self.normal_holiday + self.last_holiday

    @property
    def workday(self):
        return self.normal_workday + self.normal_workday
