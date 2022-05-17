# coding: utf-8
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Numeric, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = 'user'

    user_name = Column(String(100))
    user_password = Column(String(100))
    id = Column(String(100), primary_key=True)


class Quiz(Base):
    __tablename__ = 'quiz'

    quiz_name = Column(String(100))
    id = Column(String(100), primary_key=True)
    user_id = Column(ForeignKey('user.id'))
    date_creation = Column(DateTime)

    user = relationship('User')


class Invitation(Base):
    __tablename__ = 'invitation'

    invit_url = Column(String(100), primary_key=True)
    quiz_id = Column(ForeignKey('quiz.id'))

    quiz = relationship('Quiz')


class Question(Base):
    __tablename__ = 'questions'

    quiz_id = Column(ForeignKey('quiz.id'))
    id = Column(String(100), primary_key=True)
    number_question = Column(Numeric)
    content = Column(String(1000))

    quiz = relationship('Quiz')


class Response(Base):
    __tablename__ = 'responses'

    question_id = Column(ForeignKey('questions.id'))
    id = Column(String(100), primary_key=True)
    content = Column(String(1000))
    is_true = Column(Boolean)

    question = relationship('Question')
