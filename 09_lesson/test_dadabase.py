from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base


db_connection_string = "postgresql://postgres:1@localhost:5432/postgres"
db = create_engine(db_connection_string, echo=True)

engine = create_engine(db_connection_string)
Session = sessionmaker(bind=engine)
Base = declarative_base()

# Subject model
class Subject(Base):
    __tablename__ = 'subject'

    subject_id = Column(Integer, primary_key=True)
    subject_title = Column(String)

# Тест на добавление предмета
def test_add_subject():
    session = Session()
    subject = Subject(subject_id=100, subject_title="Mathematics")
    session.add(subject)
    session.commit()

    saved = session.query(Subject).filter_by(subject_id=100).first()
    assert saved.subject_title == "Mathematics"

    session.delete(saved)
    session.commit()
    session.close()

# Тест на изменение
def test_update_subjects():
    session = Session()
    subject = Subject(subject_id=100, subject_title="Mathematics")
    session.add(subject)
    session.commit()

    saved = session.query(Subject).filter_by(subject_id=100).first()
    assert saved.subject_title == "Mathematics"
    subject.subject_title = "Arithmetic"
    session.commit()
    saved = session.query(Subject).filter_by(subject_id=100).first()
    assert saved.subject_title == "Arithmetic"

    session.delete(saved)
    session.commit()
    session.close()

# Тест на удаление
def test_delete_subjects():
    session = Session()
    subject = Subject(subject_id=100, subject_title="Mathematics")
    session.add(subject)
    session.commit()

    saved = session.query(Subject).filter_by(subject_id=100).first()
    assert saved.subject_title == "Mathematics"

    session.delete(saved)
    session.commit()
    saved = session.query(Subject).filter_by(subject_id=100).first()
    assert saved is None

    session.close()
