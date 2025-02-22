from db import session
from models import Group, Student, Mark, Subject, Teacher
import logging
from faker import Faker
from sqlalchemy import func
from tabulate import tabulate

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")


def select_1() -> None:
    """Query 1: Get the top 5 students with the highest average mark in all subjects."""
    try:
        result = (
            session.query(Student.name, func.avg(Mark.mark))
            .join(Mark, Student.id == Mark.student_id)
            .group_by(Student.name)
            .order_by(func.avg(Mark.mark).desc())
            .limit(5)
            .all()
        )
        table = tabulate(result, tablefmt="grid")
        logging.info("\n" + table)
        return result
    except Exception as e:
        logging.error(f"Error querying the database: {e}")
    finally:
        session.close()


def select_2(sub_id: int) -> None:
    """Query 2: Get the student with the highest average mark in a specific subject."""
    try:
        result = (
            session.query(Student.name, func.avg(Mark.mark))
            .join(Mark, Student.id == Mark.student_id)
            .where(Mark.subject_id == sub_id)
            .group_by(Student.id, Student.name)
            .order_by(func.avg(Mark.mark).desc())
            .limit(1)
            .all()
        )
        table = tabulate(result, tablefmt="grid")
        logging.info("\n" + table)
        return result
    except Exception as e:
        logging.error(f"Error querying the database: {e}")
    finally:
        session.close()


def select_3(sub_id: int) -> None:
    """Query 3: Get the average mark in groups for a specific subject."""
    try:
        result = (
            session.query(Group.name, func.avg(Mark.mark), Subject.name)
            .join(Student, Group.id == Student.group_id)
            .join(Mark, Student.id == Mark.student_id)
            .join(Subject, Mark.subject_id == Subject.id)
            .where(Mark.subject_id == sub_id)
            .group_by(Group.id, Group.name, Subject.name)
            .all()
        )
        table = tabulate(result, tablefmt="grid")
        logging.info("\n" + table)
        return result
    except Exception as e:
        logging.error(f"Error querying the database: {e}")
    finally:
        session.close()


def select_4() -> None:
    """Query 4: Get the average mark in the stream (across all marks)."""
    try:
        result = session.query(func.avg(Mark.mark)).all()
        table = tabulate(result, tablefmt="grid")
        logging.info("\n" + table)
        return result
    except Exception as e:
        logging.error(f"Error querying the database: {e}")
    finally:
        session.close()


def select_5(lector_id: int) -> None:
    """Query 5: Get the subjects taught by a specific teacher."""
    try:
        result = (
            session.query(Subject.name, Teacher.name)
            .join(Teacher, Subject.teacher_id == Teacher.id)
            .where(Teacher.id == lector_id)
            .all()
        )
        table = tabulate(result, tablefmt="grid")
        logging.info("\n" + table)
        return result
    except Exception as e:
        logging.error(f"Error querying the database: {e}")
    finally:
        session.close()


def select_6(class_id: int) -> None:
    """Query 6: Get the list of students in a specific group."""
    try:
        result = (
            session.query(Group.name, Student.name)
            .join(Student, Group.id == Student.group_id)
            .where(Group.id == class_id)
            .all()
        )
        table = tabulate(result, tablefmt="grid")
        logging.info("\n" + table)
        return result
    except Exception as e:
        logging.error(f"Error querying the database: {e}")
    finally:
        session.close()


def select_7(sub_id: int, class_id: int) -> None:
    """Query 7: Get the marks of students in a specific group for a specific subject."""
    try:
        result = (
            session.query(Group.name, Subject.name, Student.name, Mark.mark)
            .join(Mark, Mark.subject_id == Subject.id)
            .join(Student, Mark.student_id == Student.id)
            .join(Group, Group.id == Student.group_id)
            .filter(Subject.id == sub_id, Group.id == class_id)
            .order_by(Group.name)
            .all()
        )
        table = tabulate(result, tablefmt="grid")
        logging.info("\n" + table)
        number_of_students = len(result)
        logging.info(number_of_students)
        return result
    except Exception as e:
        logging.error(f"Error querying the database: {e}")
    finally:
        session.close()


def select_8() -> None:
    """Query 8: Get the average mark given by a specific teacher across their subjects."""
    try:
        result = (
            session.query(Teacher.name, func.avg(Mark.mark))
            .join(Subject, Teacher.id == Subject.teacher_id)
            .join(Mark, Subject.id == Mark.subject_id)
            .group_by(Teacher.name)
            .all()
        )
        table = tabulate(result, tablefmt="grid")
        logging.info("\n" + table)
        return result
    except Exception as e:
        logging.error(f"Error querying the database: {e}")
    finally:
        session.close()


def select_9(pupil_id: int) -> None:
    """Query 9: Get the list of subjects attended by a specific student."""
    try:
        result = (
            session.query(Subject.name, Student.name)
            .join(Mark, Subject.id == Mark.subject_id)
            .join(Student, Mark.student_id == Student.id)
            .where(Student.id == pupil_id)
            .group_by(Subject.name, Student.name)
            .all()
        )
        table = tabulate(result, tablefmt="grid")
        logging.info("\n" + table)
        return result
    except Exception as e:
        logging.error(f"Error querying the database: {e}")
    finally:
        session.close()


def select_10(pupil_id: int, lector_id: int) -> None:
    """Query 10: Get the list of subjects taught by a specific teacher to a specific student."""
    try:
        result = (
            session.query(Subject.name, Student.name, Teacher.name)
            .join(Mark, Subject.id == Mark.subject_id)
            .join(Student, Mark.student_id == Student.id)
            .join(Teacher, Subject.teacher_id == Teacher.id)
            .where(Student.id == pupil_id, Teacher.id == lector_id)
            .group_by(Subject.name, Student.name, Teacher.name)
            .all()
        )
        table = tabulate(result, tablefmt="grid")
        logging.info("\n" + table)
        return result
    except Exception as e:
        logging.error(f"Error querying the database: {e}")
    finally:
        session.close()


if __name__ == "__main__":
    select_1()
    select_2(1)
    select_3(1)
    select_4()
    select_5(1)
    select_6(1)
    select_7(7, 2)
    select_8()
    select_9(36)
    select_10(3, 2)
