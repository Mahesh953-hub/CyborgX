"""
@CyborgXUpdates
"""
from sqlalchemy import Column, String

from . import BASE, SESSION


class Gdrive(BASE):
    __tablename__ = "cygdrive"
    cyborg = Column(String(50), primary_key=True)

    def __init__(self, cyborg):
        self.cyborg = cyborg


Gdrive.__table__.create(checkfirst=True)


def is_folder(folder_id):
    try:
        return SESSION.query(Gdrive).filter(Gdrive.lion == str(folder_id))
    except BaseException:
        return None
    finally:
        SESSION.close()


def gparent_id(folder_id):
    adder = SESSION.query(Gdrive).get(folder_id)
    if not adder:
        adder = Gdrive(folder_id)
    SESSION.add(adder)
    SESSION.commit()


def get_parent_id():
    try:
        return SESSION.query(Gdrive).all()
    except BaseException:
        return None
    finally:
        SESSION.close()


def rmparent_id(folder_id):
    note = SESSION.query(Gdrive).filter(Gdrive.lion == folder_id)
    if note:
        note.delete()
        SESSION.commit()
