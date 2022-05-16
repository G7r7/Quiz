# coding: utf-8
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Numeric, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class UserTable(Base):
    __tablename__ = 'user_table'

    user_name = Column(String(100))
    user_password = Column(String(100))
    id = Column(String(100), primary_key=True)


class QuizTable(Base):
    __tablename__ = 'quiz_table'

    quiz_name = Column(String(100))
    id = Column(String(100), primary_key=True)
    user_id = Column(ForeignKey('user_table.id'))
    date_creation = Column(DateTime)

    user = relationship('UserTable')


class Invitation(Base):
    __tablename__ = 'invitation'

    invit_url = Column(String(100), primary_key=True)
    quiz_id = Column(ForeignKey('quiz_table.id'))

    quiz = relationship('QuizTable')


class Question(Base):
    __tablename__ = 'questions'

    quiz_id = Column(ForeignKey('quiz_table.id'))
    id = Column(String(100), primary_key=True)
    number_question = Column(Numeric)
    content = Column(String(1000))

    quiz = relationship('QuizTable')


class Response(Base):
    __tablename__ = 'responses'

    question_id = Column(ForeignKey('questions.id'))
    id = Column(String(100), primary_key=True)
    content = Column(String(1000))
    is_true = Column(Boolean)

    question = relationship('Question')
