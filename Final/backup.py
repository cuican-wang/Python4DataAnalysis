from bs4 import BeautifulSoup as Soup
import urllib, requests, re, pandas as pd

base_url = 'http://www.indeed.com/jobs?q=data+scientist&jt=fulltime&sort='
sort_by = 'date'
start_from = '&start='
location = ''

pd.set_option('max_colwidth',500)
df = pd.DataFrame()

for page in range(0,101): # page from 1 to 100 (last page we can scrape is 100)
    page = page * 10
    url = "%s%s%s%d" % (base_url, sort_by, start_from, page) # get full url
    # print(url)
    target = Soup(urllib.request.urlopen(url), "lxml")

    targetElements = target.findAll('div', attrs={'class' : ' row result'}) # we're interested in each row (= each job)
#  trying to get each specific job information (such as company name, job title, urls, ...)
    for elem in targetElements:
        comp_name = elem.find('span', attrs={'itemprop':'name'}).getText().strip()
        job_title = elem.find('a', attrs={'class':'turnstileLink'}).attrs['title']
        home_url = "http://www.indeed.com"
        job_link = "%s%s" % (home_url,elem.find('a').get('href'))
        job_addr = elem.find('span', attrs={'itemprop':'addressLocality'}).getText()
        job_posted = elem.find('span', attrs={'class': 'date'}).getText()

        comp_link_overall = elem.find('span', attrs={'itemprop':'name'}).find('a')
        if comp_link_overall != None: # if company link exists, access it. Otherwise, skip.
            comp_link_overall = "%s%s" % (home_url, comp_link_overall.attrs['href'])
        else: comp_link_overall = None
        # add a job info to our data frame
        df = df.append({'comp_name': comp_name, 'job_title': job_title, 'job_link': job_link, 'job_posted': job_posted, 'overall_link': comp_link_overall, 'job_location': job_addr, 'overall_rating': None, 'wl_bal_rating': None, 'benefit_rating': None, 'jsecurity_rating': None, 'mgmt_rating': None, 'culture_rating': None }, ignore_index=True)

df.to_csv('C:/Users/Wang/Desktop/Python4DataAnalysis/Final/indeed_df.csv', encoding='utf-8')

df_received = df

for i in range(0,len(df_received)): # get all the company details (
    target_comp_name = df_received.iloc[i]['comp_name']

    url_2nd = df.iloc[i]['overall_link']
    if url_2nd != None:
        target_2nd = Soup(urllib.request.urlopen(url_2nd), "lxml")
        comp_logo = target_2nd.find("div", {"id": "cmp-header-logo"}).find('img')
        if comp_logo != None:
            comp_logo = target_2nd.find("div", {"id": "cmp-header-logo"}).find('img').attrs['src']

        else: comp_logo = None # total 6 ratings: overall rating, work-life balance rating, compensation / benefit rating, job security rating, management rating, company culture rating

        comp_rating_overall = target_2nd.find("span", {"class": "cmp-star-large-on"}).attrs['style']
        wl_bal_rating = target_2nd.find("dl", {"id": "cmp-reviews-attributes"}).find_all("span", {"class": "cmp-star-on"})[0].attrs['style']
        benefit_rating = target_2nd.find("dl", {"id": "cmp-reviews-attributes"}).find_all("span", {"class": "cmp-star-on"})[1].attrs['style']
        jsecurity_rating = target_2nd.find("dl", {"id": "cmp-reviews-attributes"}).find_all("span", {"class": "cmp-star-on"})[2].attrs['style']
        mgmt_rating = target_2nd.find("dl", {"id": "cmp-reviews-attributes"}).find_all("span", {"class": "cmp-star-on"})[3].attrs['style']
        culture_rating = target_2nd.find("dl", {"id": "cmp-reviews-attributes"}).find_all("span", {"class": "cmp-star-on"})[4].attrs['style']

        # Some regular expression stuffs to remove unnecessary characters
        comp_rating_overall = re.sub('[width: ]', '', comp_rating_overall)
        comp_rating_overall = re.sub('[px;]', '', comp_rating_overall)
        comp_rating_overall = round((float(comp_rating_overall)*5.0)/120, 1)
        wl_bal_rating = re.sub('[width: ]', '', wl_bal_rating)
        wl_bal_rating = re.sub('[px]', '', wl_bal_rating)
        wl_bal_rating = round((float(wl_bal_rating)*5.0)/86, 1) # 86 pixel

        benefit_rating = re.sub('[width: ]', '', benefit_rating)
        benefit_rating = re.sub('[px]', '', benefit_rating)
        benefit_rating = round((float(benefit_rating)*5.0)/86, 1)

        jsecurity_rating = re.sub('[width: ]', '', jsecurity_rating)
        jsecurity_rating = re.sub('[px]', '', jsecurity_rating)
        jsecurity_rating = round((float(jsecurity_rating)*5.0)/86, 1)

        mgmt_rating = re.sub('[width: ]', '', mgmt_rating)
        mgmt_rating = re.sub('[px]', '', mgmt_rating)
        mgmt_rating = round((float(mgmt_rating)*5.0)/86, 1)

        culture_rating = re.sub('[width: ]', '', culture_rating)
        culture_rating = re.sub('[px]', '', culture_rating)
        culture_rating = round((float(culture_rating)*5.0)/86, 1)

        # Store cleaned characters into data frame
        df_received.loc[ df_received['comp_name'] == target_comp_name, 'overall_rating'] = comp_rating_overall
        df_received.loc[ df_received['comp_name'] == target_comp_name, 'wl_bal_rating'] = wl_bal_rating
        df_received.loc[ df_received['comp_name'] == target_comp_name, 'benefit_rating'] = benefit_rating
        df_received.loc[ df_received['comp_name'] == target_comp_name, 'jsecurity_rating'] = jsecurity_rating
        df_received.loc[ df_received['comp_name'] == target_comp_name, 'mgmt_rating'] = mgmt_rating
        df_received.loc[ df_received['comp_name'] == target_comp_name, 'culture_rating'] = culture_rating

df_received.to_csv('C:/Users/Wang/Desktop/Python4DataAnalysis/Final/indeed_received.csv', encoding='utf-8')