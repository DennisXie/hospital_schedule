import datetime
from model.po.assignment_po import AssignmentPo


class AssignmentRepo(object):

    @classmethod
    def generate_month(cls, session, year: int, month: int) -> list[AssignmentPo]:
        cur = datetime.date(year, month, 1)
        assignments: list[AssignmentPo] = []
        while cur.month == month:
            holiday = cur.weekday() >= 5
            assignment = AssignmentPo(date=cur, doctor_id=None, holiday=holiday, ignore=False)
            assignments.append(assignment)
            cur = cur + datetime.timedelta(days=1)
        session.add_all(assignments)
        return assignments

    @classmethod
    def find_by_month(cls, session, year: int, month: int) -> list[AssignmentPo]:
        start = datetime.date(year, month, 1)
        next_month = start + datetime.timedelta(days=31)
        end = next_month - datetime.timedelta(next_month.day)
        return session.query(AssignmentPo).filter(AssignmentPo.date.between(start, end)).all()

    @classmethod
    def find_and_create_not_exist_by_month(cls, session, year: int, month: int) -> list[AssignmentPo]:
        assignments = cls.find_by_month(session, year, month)
        if len(assignments):
            return assignments
        else:
            cls.generate_month(session, year, month)
            return cls.find_by_month(session, year, month)

    @classmethod
    def find_one_by_date(cls, session, date: datetime.date):
        return session.query(AssignmentPo).filter(AssignmentPo.date == date).one_or_none()

    @classmethod
    def find_one_by_id(cls, session, _id: int):
        return session.query(AssignmentPo).filter(AssignmentPo.id == _id).one_or_none()

    @classmethod
    def update_by_date(cls, session, date: datetime.date, _update: AssignmentPo):
        session.query(AssignmentPo).filter(AssignmentPo.date == date).update({
            AssignmentPo.holiday: _update.holiday,
            AssignmentPo.ignore: _update.ignore,
            AssignmentPo.doctor_id: _update.doctor_id
        })

    @classmethod
    def update_by_id(cls, session, _id: int, _update: AssignmentPo):
        session.query(AssignmentPo).filter(AssignmentPo.id == _id).update({
            AssignmentPo.holiday: _update.holiday,
            AssignmentPo.ignore: _update.ignore,
            AssignmentPo.doctor_id: _update.doctor_id
        })


if __name__ == "__main__":
    from base import Session
    with Session() as _session:
        testassignments = AssignmentRepo.find_and_create_not_exist_by_month(_session, 2022, 9)
        print(len(testassignments))
        _session.commit()
