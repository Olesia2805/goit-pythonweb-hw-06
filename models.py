from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Float, Boolean, ForeignKey, Date

Base = declarative_base()


class Student(Base):
    __tablename__ = "students"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50))
    group_id: Mapped["Group"] = relationship("Group", back_populates="students")


class Subject(Base):
    __tablename__ = "subjects"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    teacher_id: Mapped["Teacher"] = relationship("Teacher", back_populates="subjects")


class Group(Base):
    __tablename__ = "groups"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))


class Teacher(Base):
    __tablename__ = "teachers"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))


class Marks(Base):
    __tablename__ = "marks"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    mark: Mapped[int] = mapped_column(Integer)
    date: Mapped[Date] = mapped_column(Date)
    student_id: Mapped["Student"] = relationship("Student", back_populates="marks")
    subject_id: Mapped["Subject"] = relationship("Subject", back_populates="marks")
