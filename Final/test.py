from bs4 import BeautifulSoup as Soup
import urllib.request
import pandas as pd
import re
from nltk.corpus import stopwords

city = ['Boston']
others = ['__2c-MA&page=']

program_languages=['bash','r','python','java','c++','ruby','perl','matlab','javascript','scala','php']
analysis_software=['excel','tableau','d3.js','sas','spss','d3','saas','pandas','numpy','scipy','sps','spotfire','scikits.learn','splunk','powerpoint','h2o']
bigdata_tool=['linux','hadoop','mapreduce','spark','pig','hive','shark','oozie','zookeeper','flume','mahout']
databases=['sql','nosql','hbase','cassandra','mongodb','mysql','mssql','postgresql','oracle db','rdbms']
degree = ["master","ph.d","bachelor"]
overall= program_languages + analysis_software + bigdata_tool + databases + degree
overallDict = dict((el, 0) for el in overall)
list1 = sorted(overallDict.keys())
list2 = ['jobTitle','compName','cmpRating','cmpReviewsAmount','cmpEmployees','jobCity','jobRegion','jobState','postDate','job_url']
list2.extend(list1)
df = pd.DataFrame(columns=list2)
n = 0
i = 1

def getSoup(url):
    req = urllib.request.Request(url)
    # print(req)
    req.add_header("User-Agent",
                   "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36")

    response = urllib.request.urlopen(req)
    soup = Soup(response, 'lxml')
    return soup

for city in city:
    base_url = 'https://www.monster.com/jobs/search/Full-Time_8?q=Data-Scientist&where='
    url = "%s%s%s" % (base_url,city,others[n])
    # print(url)
    # print(soup)
    totalPages = int(getSoup(url).find('input',id='totalPages')['value'])
    print(totalPages)

    page = 1
    url = "%s%s%s%d" % (base_url, city, others[n], page)
        # print(url)
    soup = getSoup(url)
    targetElements = soup.find_all(attrs ={"class":"js_result_row"})
        #print(targetElements)
    for elem in targetElements:
            # print('-'*30)
            # print(elem)
        overallDict = dict((el, 0) for el in overall)
        listValue = []
        jobTitle = elem.find(attrs = {"itemprop":"title"}).getText()
            # print(jobTitle)
        compName = elem.find(attrs = {"itemprop":"name"}).getText()
        jobRegion = elem.find(attrs = {"itemprop":"addressLocality"}).getText()
        jobState = elem.find(attrs={"itemprop": "addressRegion"}).getText()
        postDate = elem.find('time').get('datetime')
        job_url = elem.find('h2').find('a').get('href')
        print(job_url)
            #print(jobTitle,compName, city,jobRegion,jobState,postDate,job_url)

            # get job description from job url
        jobSoup = getSoup(job_url)
        try:
            jobDescription = jobSoup.find(attrs = {"itemprop":"description"}).getText()
        except:
            continue

        text = re.sub("[^a-zA-Z+3Ph.D]", " ", jobDescription)
        text = text.lower().split()
        stops = set(stopwords.words("english"))  # filter out stop words in english language
        text = [w for w in text if not w in stops]
        text = list(set(text))
        keywords = [str(word) for word in text if word in overall]
        for w in keywords:
            overallDict[w] = 1
        print(overallDict)
            # get company rating from indeed.com
        base_url = 'http://www.indeed.com/cmp/'
        url = ('%s%s' % (base_url,compName))
        try:
            cmpSoup = getSoup(url)
        except:
            continue
        #print(url)
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
        #print(url)
        try:
            cmpEmployees = cmpSoup.find(attrs = {"id":"cmp-company-details-sidebar"}).find(string=re.compile("Employees")).next.getText()
        except:
            cmpEmployees = 'NA'
        listValue.append(jobTitle)
        listValue.append(compName)
        listValue.append(cmpRating)
        listValue.append(cmpReviewsAmount)
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
            # print(jobDescription)
            # print('-'*100)
            # print('\r')
    n += 1  # put at the end of the loop

df.to_csv('C:/Users/Wang/Desktop/Python4DataAnalysis/Final/test1.csv', encoding='utf-8')