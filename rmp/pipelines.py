# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy.orm import sessionmaker
from rmp.models import Professor, Rating, db_connect, create_table
import os

class RmpPipeline(object):

    def __init__ (self):
        engine = db_connect(os.getcwd())
        create_table(engine)
        Session = sessionmaker(bind = engine)
        self.session = Session()


    def process_item(self, item, spider):
                # problem here.

        if 'pname' in item:
            professor = Professor(**item)
            try:
                self.session.add(professor)
            except:
                self.session.rollback()
                raise
        else:
            rating = Rating(**item)
            try:
                self.session.add(rating)
            except:
                self.session.rollback()
                raise
        self.session.commit()
        

        return item
