# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field
from scrapy.loader.processors import Join


class ProfessorItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    tid = Field()
    sid = Field()

    pfname = Field()
    plname = Field()
    pname = Field(output_processor = Join())
    n_rating = Field()
    quality = Field()
    university = Field()
    department = Field()
    difficulty = Field()
    tags = Field()


class RatingItem(Item):

    rid = Field()
    tid = Field()
    sid = Field()

    attendance = Field()
    helpCount = Field()
    notHelpCount = Field()

    rClarity = Field()
    rClass = Field()
    rComments = Field()
    rDate = Field()
    rEasy = Field()
    rErrorMsg = Field()
    rHelpful = Field()
    rInterest = Field()
    rOverall = Field()
    rStatus = Field()
    rTextBookUse = Field()
    rWouldTakeAgain = Field()

    takenForCredit = Field()
    teacher = Field()
    teacherGrade = Field()
    tags = Field()
