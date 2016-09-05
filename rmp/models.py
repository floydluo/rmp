import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, String, Integer, Float, Table, Text

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


def sdb_connect(basedir, name = "data"):
    # For SQLite database.
    return create_engine('sqlite:///' + os.path.join(basedir, name + '.sqlite'))


def mdb_connect():
    # For MySQL database.
    MySQL_DB = 'mysql+mysqlconnector://root:woai19950920@localhost:3306/rmp?charset=utf8'
    return create_engine(MySQL_DB)


Base = declarative_base()

def create_table(engine):
    Base.metadata.create_all(engine)

class Professor(Base):
    __tablename__ = 'professors'

    id = Column(Integer, primary_key = True)
    tid = Column(Integer)
    sid = Column(Integer)

    pfname = Column(String(30))
    plname = Column(String(30))
    pname = Column(String(50))
    department = Column(String(30))
    university = Column(String(30))

    quality = Column(Float)
    difficulty = Column(Float)
    n_rating = Column(Integer)

    tags = Column(Text)

    def __repr__(self):
        return "<Professor(name = %r)>" %self.pname


class Rating(Base):
    __tablename__ = 'ratings'

    id = Column(Integer, primary_key = True)

    rid = Column(Integer)
    tid = Column(Integer)
    sid = Column(Integer)

    attendance = Column(String(30))
    helpCount = Column(Integer)
    notHelpCount = Column(Integer)

    rClarity = Column(Float)
    rClass = Column(String(30))
    rComments = Column(Text)
    rDate = Column(String(30))
    rEasy = Column(Float)
    rErrorMsg = Column(String(30))
    rHelpful = Column(Float)
    rInterest = Column(String(30))
    rOverall = Column(Float)
    rStatus = Column(Integer)
    rTextBookUse = Column(String(30))
    rWouldTakeAgain = Column(String(30))

    takenForCredit = Column(String(30))
    teacher = Column(String(30))
    teacherGrade = Column(String(30))

    tags = Column(Text)

    def __repr__(self):
        return "<Rating(rOverall = %r)>" %self.rOverall
