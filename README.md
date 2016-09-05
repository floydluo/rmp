# Rate My Professor

#### 1 Install Scrapy and Packages
* 1.1 Immerse in `Anaconda`
* 1.2 Install `Scrapy`
* 1.3 Install `mysql-connector-python`

#### 2 Start RMP Project
* 2.1 Start project by `startproject`
* 2.2 Walk through the project

#### 3 Scrutinize the Website
* 3.1 Visit [ratemyprofessors.com](http://www.ratemyprofessors.com)
* 3.2 Construct items.
* 3.3 Catch the Packages

#### 4 Find the correct URLs
* 4.1 Yield Professor URLs
* 4.2 Yield Rating URLs

#### 5 Raise a Spider
* 5.1 Start_urls
* 5.2 Parse and Response
* 5.3 Selector
* 5.4 ItemLoader

#### 6 Store in MySQL
* 6.1 Build models
* 6.2 Evoke pipeline

#### 7 Set, Configurate and Run
* 7.1 Settings
* 7.2 Configuration
* 7.3 Run on Terminal

## 1 Install Scrapy and Packages
##### 1.1 Immerse in Anaconda

`Anaconda` is a miraculous python distribution which can spare us uncountable trouble when we want to install some python packages.

From Wikipedia:
>Anaconda is a freemium open source distribution of the Python and R programming languages for large-scale data processing, predictive analytics, and scientific computing, that aims to simplify package management and deployment.

You can install it from [Anaconda Website](https://www.continuum.io/downloads).

##### 1.2 Install Scrapy
With Anaconda installed, you can download scrapy in this way:

`$ conda install scrapy`

##### 1.3 Install Packages
Even Anaconda has numbers of packages, we still need another package name `mysql-connector-python`, which is used to connect MySQL and Python.
To install it:

`$ conda install mysql-connector-python`
****
*Some time these package may have conflicts with each other, even themselves (for difference versions), which might cause the chaos to Computer System.*

*__To avoid this potential problem, you can make `virtual environments` via `conda` or `virtualenv` for each project.__*
***

## 2 Start RMP Project

This project is a scrapy project which scrape the professors and their ratings information from website: [ratemyprofessors.com](http://www.ratemyprofessors.com).

This project only focuses on the professors come from [University of Delaware](http://www.udel.edu).

We want to scrape every pieces of information. `Scrapy` is suitable for this task. So, let's begin with `scrapy` first.

##### 2.1 Start project by `startproject`

On terminal, change the directory to your project directory, then use this command to start your project with the name `rmp`:

`$ scrapy startproject rmp`

A file is generated, which is the essential framework of scrapy project.

```
 $ scrapy startproject rmp
New Scrapy project 'rmp', using template.....created in:
You can start your first spider with:
    cd rmp
    scrapy genspider example example.com

$ tree # you can install this command via brew.
.
└── rmp
    ├── rmp
    │   ├── __init__.py
    │   ├── items.py
    │   ├── pipelines.py
    │   ├── settings.py
    │   └── spiders
    │       ├── __init__.py
    └── scrapy.cfg
```
However, to deal with the whole project, you must change the directory to next `rmp`.
Do it as scrapy indicate:

`$ cd rmp`

Use `tree` again, you will see:
```
$ tree
.
├── rmp
│   ├── __init__.py
│   ├── items.py
│   ├── pipelines.py
│   ├── settings.py
│   └── spiders
│       ├── __init__.py
└── scrapy.cfg
```
This is the default directory location where scrapy run the whole project.

##### 2.1 Walk Trough the project
This should be a brief introduction to these files.

## 3 Scrutinize the website
##### 3.1 Visit [ratemyprofessors.com](http://www.ratemyprofessors.com)
This part would present some graphs of this website, and highlight the parts and data we want to scrape.

However, graphs are not so easy to generate.

This part, to be continued...

##### 3.2 Construct items
When we have the object to scrape, we should write a container to hold the data we scrape, this is the reason we have the file: `items.py`

`from scrapy import Item, Field`

then we construct two classes, one is Professor, another is Rating.

```
class Professor(Item):
      tid = Field()
      sid = Field()

      pfname = Field()
      plname = Field()
      ...

class Rating(Item):
      rid = Field()
      tid = Field()
      sid = Field()
      attendance = Field()
      ...
```
Some fields are skipped here.
`Item` is much like python's dictionary. And `Field` represents the key.

If we have dictionary, let's call it `dic`. `dic` has the same keys as an Item, let's call it `Professor`, you can make an object in this way:

`Pro = Professor(**dic)`



##### 3.3 Catch the Packages
This part should be the story which tells what I experienced to find the right URLs to get correct data.

This website is a little strange, These are now way you can find the data from its main response.

With chrome's developer tool, eventually, I found three important kinds of URLs to get the data I wanted.



__start_url__
```
http://search.mtvnservices.com/typeahead/suggest/?solrformat=true&rows=10&callback=noCB&q=*%3A*+AND+schoolid_s%3A1094&defType=edismax&qf=teacherfullname_t%5E1000+autosuggest&bf=pow(total_number_of_ratings_i%2C2.1)&sort=teacherlastname_sort_s+asc&siteName=rmp&rows=4000&start=0&fl=pk_id+teacherfirstname_t+teacherlastname_t+total_number_of_ratings_i+averageratingscore_rf+schoolid_s
```

__professor_urls__

```
https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1427675
```

__rating_urls__
```
http://www.ratemyprofessors.com/paginate/professors/ratings?tid=%d&page=%d
```


## 4 Find the correct URLs

##### 4.1 Yield Professor URLs

##### 4.2 Yield Rating URLs




## 5 Raise a Spider

##### 5.1 Start_urls

##### 5.2 Parse and Response

##### 5.3 Selector

##### 5.4 ItemLoader



## 6 Store in MySQL

##### 6.1.1 Build models

##### 6.2 Evoke pipeline










## 7 Set, Configure and Run

##### 7.1 Set the Spider's behavior
We have `settings.py` to set some variables.

Some important ones:
```
BOT_NAME = 'rmp'
SPIDER_MODULES = ['rmp.spiders']
NEWSPIDER_MODULE = 'rmp.spiders'

# these three variables are generated automatically by startproject

ROBOTSTXT_OBEY = False
# I set this variable to False in order to enable the spider crawl the website.


DEFAULT_REQUEST_HEADERS = {
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36",
    "Accept-Encoding": "gzip,deflate,sdch",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-TW;q=0.2",
}
# the request_headers make your bot a little more like a browser, a little more like human beings.

ITEM_PIPELINES = {
    'rmp.pipelines.RmpPipeline': 300,
}
# this indicate the pipeline to use. 300 is a number that indicate the order.

```

##### 7.2 Configuration file
There is a file named `scrapy.cfg`.

Its content is also generated automatically, you can add more things if you want your spider more functional.

```
[settings]
default = rmp.settings

[deploy]
project = rmp
```

And its content just means tiny things: __follow the orders in `settings.py`, deploy the project `rmp`.


##### 7.3 Run it in Terminal
To run this project, make sure your terminal is of right directory.

And use this command:

`$ scrapy crawl rmp`

`rmp` is the spider's name.

Then the terminal will run this project. The items you scraped will be presented in the screen.

This process will last about 4 minutes. The summary of this project is shown as this:


```
2016-09-05 16:16:52 [scrapy] INFO: Closing spider (finished)
2016-09-05 16:16:52 [scrapy] INFO: Dumping Scrapy stats:
{'downloader/request_bytes': 4309137,
 'downloader/request_count': 7596,
 'downloader/request_method_count/GET': 7596,
 'downloader/response_bytes': 67137940,
 'downloader/response_count': 7596,
 'downloader/response_status_count/200': 7596,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2016, 9, 5, 8, 16, 52, 396526),
 'item_scraped_count': 58641,
 'log_count/DEBUG': 66238,
 'log_count/INFO': 22,
 'request_depth_max': 2,
 'response_received_count': 7596,
 'scheduler/dequeued': 7596,
 'scheduler/dequeued/memory': 7596,
 'scheduler/enqueued': 7596,
 'scheduler/enqueued/memory': 7596,
 'start_time': datetime.datetime(2016, 9, 5, 8, 1, 43, 981891)}
2016-09-05 16:16:52 [scrapy] INFO: Spider closed (finished)
```
Totally, `58641` items were scraped, `7596` requests were sent.
