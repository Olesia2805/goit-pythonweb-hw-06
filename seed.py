from db import session
from models import Group, Student, Mark, Subject, Teacher
import logging
from faker import Faker

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

GROUPS = ["MCS4", "MDA2", "CS1"]
SUBJECTS = [
    "Math",
    "Python",
    "C++",
    "Java",
    "JavaScript",
    "HTML/CSS",
    "React",
    "English",
]
fake = Faker("uk_UA")


def seed_groups(groups: list) -> None:
    """Seed groups into the database."""
    try:
        for item in groups:
            group = Group(name=item)
            session.add(group)
        session.commit()
        logging.info("Groups seeded successfully")
    except Exception as e:
        session.rollback()
        logging.error(f"Error seeding groups: {e}")
    finally:
        session.close()


def seed_students(students: int) -> None:
    """Seed students into the database."""
    try:
        group_ids = [x.id for x in session.query(Group.id).all()]
        for _ in range(students):
            student = Student(
                name=fake.name(),
                email=fake.email(),
                group_id=fake.random_element(elements=group_ids),
            )
            session.add(student)
        session.commit()
        logging.info("Students seeded successfully")
    except Exception as e:
        session.rollback()
        logging.error(f"Error seeding students: {e}")
    finally:
        session.close()


def seed_teachers(teachers: int) -> None:
    """Seed teachers into the database."""
    try:
        for _ in range(teachers):
            teacher = Teacher(name=fake.name())
            session.add(teacher)
        session.commit()
        logging.info("Teachers seeded successfully")
    except Exception as e:
        session.rollback()
        logging.error(f"Error seeding teachers: {e}")
    finally:
        session.close()


def seed_subjects(subjects: list) -> None:
    """Seed subjects into the database."""
    try:
        teachers = session.query(Teacher).all()
        if not teachers:
            raise Exception("No teachers found")

        for item in subjects:
            teacher = fake.random_element(elements=teachers)
            subject = Subject(name=item, teacher_id=teacher.id)
            session.add(subject)
        session.commit()
        logging.info("Subjects seeded successfully")
    except Exception as e:
        session.rollback()
        logging.error(f"Error seeding subjects: {e}")
    finally:
        session.close()


def seed_marks() -> None:
    """Seed marks into the database."""
    try:
        students = session.query(Student).all()
        subjects = session.query(Subject).all()
        for student in students:
            for subject in subjects:
                num_marks = fake.random_int(min=10, max=20)
                for _ in range(num_marks):
                    subject = fake.random_element(elements=subjects)
                    mark = Mark(
                        mark=fake.random_int(min=1, max=10),
                        date=fake.date_this_year(before_today=True),
                        student_id=student.id,
                        subject_id=subject.id,
                    )
                    session.add(mark)
        session.commit()
        logging.info("Marks seeded successfully")
    except Exception as e:
        session.rollback()
        logging.error(f"Error seeding marks: {e}")
    finally:
        session.close()


def fill_db():
    seed_groups(GROUPS)
    seed_students(50)
    seed_teachers(3)
    seed_subjects(SUBJECTS)
    seed_marks()


if __name__ == "__main__":
    fill_db()
