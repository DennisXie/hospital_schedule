from model.dto.assignment import Assignment
from model.po import AssignmentPo, DoctorPo
from repository import AssignmentRepo, DoctorRepo, Session


class ScheduleService(object):

    @classmethod
    def get_schedule_assignments(cls, year: int, month: int) -> list[Assignment]:
        with Session() as session:
            assignment_pos: list[AssignmentPo] = AssignmentRepo.find_and_create_not_exist_by_month(session, year, month)
            doctor_ids = [assignment.id for assignment in assignment_pos]
            doctors: list[DoctorPo] = DoctorRepo.find_by_ids(session, doctor_ids)
            doctor_map: dict[int, str] = {d.id: d.name for d in doctors}
            assignments: list[Assignment] = []
            for assignment_po in assignment_pos:
                name = doctor_map.get(assignment_po.doctor_id)
                assignment = Assignment(assignment_po.date, name, assignment_po.holiday, assignment_po.ignore)
                assignments.append(assignment)
            return assignments
