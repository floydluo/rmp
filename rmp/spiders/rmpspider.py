# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import json
import math

from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join, TakeFirst
from scrapy import Spider
from scrapy.http import Request

from rmp.items import ProfessorItem, RatingItem



class RMPSpider(Spider):
    name = 'rmp'
    start_urls = (
        "http://search.mtvnservices.com/typeahead/suggest/?solrformat=true&rows=10&callback=noCB&q=*%3A*+AND+schoolid_s%3A1094&defType=edismax&qf=teacherfullname_t%5E1000+autosuggest&bf=pow(total_number_of_ratings_i%2C2.1)&sort=teacherlastname_sort_s+asc&siteName=rmp&rows=4000&start=0&fl=pk_id+teacherfirstname_t+teacherlastname_t+total_number_of_ratings_i+averageratingscore_rf+schoolid_s",
        )

    def parse(self, response):
        base_url = "http://www.ratemyprofessors.com/"
        body = response.body.decode('utf-8')
        body = body[5:-2]
        body_dic = json.loads(body)
        docs = body_dic['response']['docs']
        for doc in docs:
            id = doc['pk_id'] 
            url = base_url + "ShowRatings.jsp?tid=%d" %id
            try:
                quality = doc['averageratingscore_rf']            
            except:
                quality = 0
            meta = {'tid' : id,
                    'n_rating' : doc['total_number_of_ratings_i'], 
                    'sid' : int(doc['schoolid_s']),
                    'pfname' : doc['teacherfirstname_t'],
                    'plname' : doc['teacherlastname_t'],
                    'quality': quality
                    }
            yield Request(url, meta = meta, callback = self.parse_prof)

    def parse_prof(self, response):
        departxpath = "//*[@id='mainContent']//div[@class='result-title']/text()"
        univerxpath = "//*[@id='mainContent']//div[@class='result-title']//a[@class='school']/text()"
        difficxpath = "//*[@id='mainContent']//div[@class='rating-breakdown']//div[@class='breakdown-header']/div[2]/div[@class='grade']/text()"
        kxpath = "//*[@id='mainContent']//div[@class='rating-breakdown']/div[2]/div[@class='tag-box']/span[@class='tag-box-choosetags']/text()"
        vxpath = "//*[@id='mainContent']//div[@class='rating-breakdown']/div[2]/div[@class='tag-box']/span[@class='tag-box-choosetags']/b/text()"

        l = ItemLoader(item = ProfessorItem(), response = response)
        l.default_output_processor = TakeFirst()
        
        l.add_value('tid', response.meta['tid'])
        l.add_value('sid', response.meta['sid'])
        l.add_value('pfname', response.meta['pfname'])
        l.add_value('plname', response.meta['plname'])
        l.add_value('pname', response.meta['pfname'])
        l.add_value('pname', response.meta['plname'])
        l.add_value('quality', response.meta['quality'])
        l.add_value('n_rating', response.meta['n_rating'])

        l.add_xpath('department', departxpath, re = 'Professor in the (.+) department')
        l.add_xpath('university', univerxpath)
        l.add_xpath('difficulty', difficxpath, MapCompose(lambda p: float(p.replace("\r\n",'').replace(' ',''))))
        
        keys = l.get_xpath(kxpath, MapCompose(lambda p: p.replace(' ','')))
        values = l.get_xpath(vxpath, MapCompose(lambda p: int(p.strip('(').strip(')'))))
        l.add_value('tags', json.dumps(dict(zip(keys, values))))

        yield l.load_item()
        n_rating = response.meta['n_rating']
        if n_rating != 0:
            tid = response.meta['tid']
            for pn in range(math.ceil(n_rating/20)):
                url = 'http://www.ratemyprofessors.com/paginate/professors/ratings?tid=%d&page=%d' %(tid, pn+1) # a int is needed here
                yield Request(url, meta = response.meta, callback = self.parse_rating)

    def parse_rating(self, response):
        body_dic = json.loads(response.body.decode('utf-8'))
        for rating in body_dic['ratings']:
            l = ItemLoader(item = RatingItem(), response = response)
            l.default_output_processor = TakeFirst()
            # error, change tid to id
            l.add_value('rid', rating['id'])
            l.add_value('tid', response.meta['tid'])
            l.add_value('sid', response.meta['sid'])

            l.add_value('attendance', rating['attendance'])
            l.add_value('helpCount', rating['helpCount'])
            l.add_value('notHelpCount', rating['notHelpCount'])
            l.add_value('rClarity', rating['rClarity'])
            l.add_value('rClass', rating['rClass'])
            l.add_value('rComments', rating['rComments'])
            l.add_value('rDate', rating['rDate'])
            l.add_value('rEasy', rating['rEasy'])
            l.add_value('rErrorMsg', rating['rErrorMsg'])
            l.add_value('rHelpful', rating['rHelpful'])
            l.add_value('rInterest', rating['rInterest'])
            l.add_value('rOverall', rating['rOverall'])
            l.add_value('rStatus', rating['rStatus'])
            l.add_value('rTextBookUse', rating['rTextBookUse'])
            l.add_value('rWouldTakeAgain', rating['rWouldTakeAgain'])
            
            l.add_value('takenForCredit', rating['takenForCredit'])
            l.add_value('teacher', rating['teacher'])
            l.add_value('teacherGrade', rating['teacherGrade'])

            keys = l.get_value(rating['teacherRatingTags'])
            values = [1]*len(keys)
            l.add_value('tags', json.dumps(dict(zip(keys,values))))
            yield l.load_item()




