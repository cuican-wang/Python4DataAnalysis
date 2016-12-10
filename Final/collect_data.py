from bs4 import BeautifulSoup as Soup
import urllib.request
import pandas as pd
import re
from nltk.corpus import stopwords
import time
import random

city = ['San-Francisco','Boston','Palo-Alto','Chicago','New-York','Washington','Seattle','Atlanta','Houston','San-Diego']
others = ['__2C-CA&page=','__2c-MA&page=','__2C-CA&page=','__2C-IL&page=','__2C-NY&page=','__2C-DC&page=','__2C-WA&page=','__2c-GA&page=','__2C-TX&page=','__2C-CA&page=']

program_languages=['bash','r','python','java','c++','ruby','perl','javascript','scala','php','c','shell']
analysis_software=['matlab','excel','tableau','d3.js','sas','spss','d3','saas','pandas','numpy','scipy','sps','spotfire','scikits.learn','splunk','powerpoint','h2o']
bigdata_tool=['linux','hadoop','mapreduce','spark','pig','hive','shark','oozie','zookeeper','flume','mahout']
databases=['sql','nosql','hbase','cassandra','mongodb','mysql','mssql','postgresql','oracle','rdbms']
# other_knowledge = ['statistics','math','']
degree = ["master","ph.d","bachelor"]
overall= program_languages + analysis_software + bigdata_tool + databases + degree # list
overallDict = dict((el, 0) for el in overall) # dictionary
list1 = sorted(overallDict.keys()) # list
list2 = ['jobTitle','cmpName','cmpRating','cmpReviewsAmount','cmpReviews','cmpEmployees','jobCity','jobRegion','jobState','postDate','job_url']
list2.extend(list1)
df = pd.DataFrame(columns=list2)
n = 0 # change city
i = 1 # for add dataframe rows
cmp_dict = {}

def getSoup(url): # get soup function
    # j = random.randint(1000, 1500) / 1000.0
    # time.sleep(j)
    req = urllib.request.Request(url)
    # print(req)
    req.add_header("User-Agent",
                   "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36")

    response = urllib.request.urlopen(req)
    soup = Soup(response, 'lxml')
    return soup
try:
    for city in city:
        base_url = 'https://www.monster.com/jobs/search/Full-Time_8?q=Data-Scientist&where='
        url = "%s%s%s" % (base_url, city, others[n])
        print('city-'*300)
        print(url)
        # print(soup)
        totalPages = int(getSoup(url).find('input', id='totalPages')['value'])
        # print(totalPages)

        for page in range(1,totalPages+1):
            url = "%s%s%s%d" % (base_url, city, others[n], page)
            print('page-'*300)
            print(url)
            # print(url)
            # try:
            soup = getSoup(url)
            # except:
            #     continue
            targetElements = soup.find_all(attrs={"class": "js_result_row"})
            for elem in targetElements:
                overallDict = dict((el, 0) for el in overall)
                listValue = []
                jobTitle = elem.find(attrs={"itemprop": "title"}).getText()
                # print(jobTitle)
                cmpName = elem.find(attrs={"itemprop": "name"}).getText()
                if cmpName not in cmp_dict.keys():
                    cmp_dict[cmpName] = 1
                    review_baseurl = 'http://www.indeed.com/cmp/'
                    review_endurl = '/reviews'
                    review_url = "%s%s%s" % (review_baseurl,cmpName,review_endurl)
                    try:
                        review_soup = getSoup(review_url)
                    except:
                        review_soup = 'NA'
                    if review_soup != 'NA':
                        try:
                            reviewElements = review_soup.find_all(attrs={"class": "cmp-review-description"})
                            cmpReviews = ''
                            for review in reviewElements:
                                # print('-'*500)
                                # print(elem.getText())
                                cmpReviews += review.getText()
                        except:
                            cmpReviews = ''
                    else:
                        cmpReviews = ''
                else:
                    cmpReviews = ''
                try:
                    jobRegion = elem.find(attrs={"itemprop": "addressLocality"}).getText()
                    jobState = elem.find(attrs={"itemprop": "addressRegion"}).getText()
                except:
                    try:
                        jobRegion = elem.find(attrs={"itemprop": "location"}).getText()
                        jobState = 'NA'
                    except:
                        continue

                postDate = elem.find('time').get('datetime')
                job_url = elem.find('h2').find('a').get('href')
                print(job_url)
                # print(jobTitle,compName, city,jobRegion,jobState,postDate,job_url)

                # get job description from job url
                try:
                    jobSoup = getSoup(job_url)
                except:
                    continue
                try:
                    jobDescription = jobSoup.find(attrs={"itemprop": "description"}).getText()
                except:
                    try:
                        jobDescription = jobSoup.find(attrs={"class": "jobview-section"}).getText()
                    except:
                        try:
                            jobDescription = jobSoup.find(attrs={"class": "JobViewJobBody"}).getText()
                        except:
                            continue

                text = re.sub("[^a-zA-Z+3Ph.Dd3.js]", " ", jobDescription)
                text = text.lower().split()
                stops = set(stopwords.words("english"))  # filter out stop words in english language
                text = [w for w in text if not w in stops]
                text = list(set(text))
                keywords = [str(word) for word in text if word in overall]
                for w in keywords:
                    overallDict[w] = 1
                print(overallDict)
                # get company rating from indeed.com
                cmp_base_url = 'http://www.indeed.com/cmp/'
                url = ('%s%s' % (cmp_base_url, cmpName))
                try:
                    cmpSoup = getSoup(url)
                except:
                    cmpSoup = 'NA'
                # print(url)
                try:
                    cmpRating = float(cmpSoup.find('span', {'class': 'cmp-average-rating'}).getText())
                except:
                    cmpRating = 'NA'

                try:
                    cmpReviewsAmount = re.split('(\d+)', cmpSoup.find(attrs={"class": "cmp-note"}).getText().split(' ')[0])
                except:
                    cmpReviewsAmount = 'NA'

                if cmpReviewsAmount != 'NA':
                    if cmpReviewsAmount[-1] == "K":
                        try:
                            cmpReviewsAmount = float(cmpReviewsAmount[1] + cmpReviewsAmount[2] + cmpReviewsAmount[3]) * 1000
                        except:
                            cmpReviewsAmount = float(cmpReviewsAmount[1]) * 1000
                    else:
                        cmpReviewsAmount = float(cmpReviewsAmount[1])
                # print(url)
                try:
                    cmpEmployees = cmpSoup.find(attrs={"id": "cmp-company-details-sidebar"}).find(
                        string=re.compile("Employees")).next.getText()
                except:
                    cmpEmployees = 'NA'
                listValue.append(jobTitle)
                listValue.append(cmpName)
                listValue.append(cmpRating)
                listValue.append(cmpReviewsAmount)
                listValue.append(cmpReviews)
                listValue.append(cmpEmployees)
                listValue.append(city)
                listValue.append(jobRegion)
                listValue.append(jobState)
                listValue.append(postDate)
                listValue.append(job_url)
                print(overallDict[x] for x in sorted(overallDict))
                listValue.extend(overallDict[x] for x in sorted(overallDict))
                df.loc[i] = listValue

                i += 1
        n += 1
                # print(jobDescription)
                # print('-'*100)
                # print('\r')
except:
    df.to_csv('C:/Users/Wang/Desktop/Python4DataAnalysis/Final/data/test_data/error7.csv', encoding='utf-8')
df.to_csv('C:/Users/Wang/Desktop/Python4DataAnalysis/Final/data/webScrepedData.csv.csv', encoding='utf-8')