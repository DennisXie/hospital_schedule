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
                assignment.id = assignment_po.id
                assignments.append(assignment)
            return assignments

    @classmethod
    def update_assignment(cls, _update: Assignment) -> Assignment:
        with Session() as session:
            doctor_po = DoctorRepo.find_one_by_name(session, _update.name)
            if doctor_po:
                _update_po = AssignmentPo(doctor_id=doctor_po.id, holiday=_update.holiday, ignore=_update.ignore)
                AssignmentRepo.update_by_id(session, _update.id, _update_po)
                return _update
            else:
                # TODO: throw doctor not exist
                pass

    @classmethod
    def schedule(cls, year: int, month: int) -> list[Assignment]:
        pass
