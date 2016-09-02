import os 

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, String, Integer, Float, Table, Text

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


def db_connect(basedir, name = "data"):
    return create_engine('sqlite:///' + os.path.join(basedir, name + '.sqlite'))


Base = declarative_base()

def create_table(engine):
    Base.metadata.create_all(engine)

class Professor(Base):
    __tablename__ = 'professors'

    id = Column(Integer, primary_key = True)
    tid = Column(Integer)
    sid = Column(Integer)

    pfname = Column(String)
    plname = Column(String)
    pname = Column(String)
    department = Column(String)
    university = Column(String)

    quality = Column(Float)
    difficulty = Column(Float)
    n_rating = Column(Integer)
    
    tags = Column(String)

    def __repr__(self):
        return "<Professor(name = %r)>" %self.pname


class Rating(Base):
    __tablename__ = 'ratings'

    id = Column(Integer, primary_key = True)

    rid = Column(Integer)
    tid = Column(Integer)
    sid = Column(Integer)

    attendance = Column(String)
    helpCount = Column(Integer)
    notHelpCount = Column(Integer)

    rClarity = Column(Float)
    rClass = Column(String)
    rComments = Column(Text)
    rDate = Column(String)
    rEasy = Column(Float)
    rErrorMsg = Column(String)
    rHelpful = Column(Float)
    rInterest = Column(String)
    rOverall = Column(Float)
    rStatus = Column(Integer)
    rTextBookUse = Column(String)
    rWouldTakeAgain = Column(String)

    takenForCredit = Column(String)
    teacher = Column(String)
    teacherGrade = Column(String)

    tags = Column(String)

    def __repr__(self):
        return "<Rating(rOverall = %r)>" %self.rOverall





    