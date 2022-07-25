from model.po.doctor_po import DoctorPo


class DoctorRepo(object):

    @classmethod
    def find_enabled(cls, session) -> list[DoctorPo]:
        return session.query(DoctorPo).filter(DoctorPo.enabled.is_(True)).all()

    @classmethod
    def find_one_by_name(cls, session, name: str) -> DoctorPo:
        return session.query(DoctorPo).filter(DoctorPo.name == name).one_or_none()

    @classmethod
    def save_all(cls, session, doctors: list[DoctorPo]):
        return session.add_all(doctors)

    @classmethod
    def save(cls, session, doctor: DoctorPo):
        return session.add(doctor)

    # TODO: add save or update

    @classmethod
    def update_by_name(cls, session, name: str, _update: DoctorPo):
        session.query(DoctorPo).filter(DoctorPo.name == name).update({
            DoctorPo.enabled: _update.enabled,
            DoctorPo.schedule: _update.schedule
        })

    @classmethod
    def update_by_id(cls, session, _id: int, _update: DoctorPo):
        session.query(DoctorPo).filter(DoctorPo.id == _id).update({
            DoctorPo.name: _update.name,
            DoctorPo.enabled: _update.enabled,
            DoctorPo.schedule: _update.schedule
        })
