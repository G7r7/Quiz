# coding: utf-8
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Numeric, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(100))
    user_password = Column(String(100))


class Quiz(Base):
    __tablename__ = 'quiz'

    id = Column(Integer, primary_key=True, index=True)
    quiz_name = Column(String(100))
    user_id = Column(ForeignKey('user.id'))
    date_creation = Column(DateTime)

    user = relationship('User')


class Invitation(Base):
    __tablename__ = 'invitation'

    id = Column(Integer, primary_key=True, index=True)
    invit_url = Column(String(100), primary_key=True)
    quiz_id = Column(ForeignKey('quiz.id'))

    quiz = relationship('Quiz')


class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True, index=True)
    quiz_id = Column(ForeignKey('quiz.id'))
    number_question = Column(Numeric)
    content = Column(String(1000))

    quiz = relationship('Quiz')


class Response(Base):
    __tablename__ = 'responses'

    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(ForeignKey('questions.id'))
    content = Column(String(1000))
    is_true = Column(Boolean)

    question = relationship('Question')
