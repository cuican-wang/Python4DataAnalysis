import oauth2 as oauth
import json,requests
from argparse import ArgumentParser
import os
import matplotlib.pyplot
import pylab
import numpy as np #just for a random color not used to analyze data


CONSUMER_KEY = "WC3zaJa2gSa8A8UkFRCn9YWvO"
CONSUMER_SECRET = "3So1Ld1muwpE2Pwt8nShw0iQL6jialgiNCtnxiiCaH5tHh4ESi"
ACCESS_KEY = "570787998-19TdCbxP2ES2IMqszhBhylnbuqqYdrwuCTXvdXp4"
ACCESS_SECRET = "jchylHmi980oWVjPumMo5Dp20oR8vF522hnGnKqquOVap"

consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)

term_0 = input("What do you want to search?")
#datetime用来分析的时候 获取当前时间 命名文件夹？或者用来规范搜索时输入的时间选项？
#datetime_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# p = ArgumentParser(usage='it is usage tip', description='this is a test')
# #根据twitter api搜索词转换规则 转换
# p.add_argument('--trump clinton', default='trump%20clinton', help='the first argument')
# p.add_argument('--two', default=2, type=int, help='the second argument')
# p.add_argument('--docs-dir', default="./", help='document directory ')
# args = p.parse_args()
#term_1 = args.term_0

count = input("How many data do you want?")

date_0 = input("What date do you want to set?:")
#date_1 = datetime.date(date_0).isoformat()

#location = input("Tweets from where do you want to see?:")

choose_time = int(input("What kind of date do you want to set? Input 1 means since date, input 2 means up to date.:"))


if choose_time==1:
    #global search_1
    integra_search = "%20since%3A" + date_0 + '&count=' + count
    search_1 = "https://api.twitter.com/1.1/search/tweets.json?q=" + term_0 + integra_search
if choose_time==2:
    #global search_1
    integra_search = "%20until%3A" + date_0 + '&count=' + count
    search_1 = "https://api.twitter.com/1.1/search/tweets.json?q=" + term_0 + integra_search
else:
    search_1 = "https://api.twitter.com/1.1/search/tweets.json?q=" + term_0 + "%20until%3A" + date_0 + '&count=' + count
    print("Your input is wrong, please input again")
    #Should be a recursive function?

response, data = client.request(search_1)

str_response = data.decode('utf-8')
tweets = json.loads(str_response)

#function to check if folder is present if not create it
def Save_Json():
    path = input("Please input a path to save data:")
    def check_folder():
        if not os.path.exists(path):
            os.makedirs(path)

    check_folder()
    #Save tweets data in json
    json.dump(tweets, open(path + '\\' + term_0 + '.dat', 'w'))

#Analysis one: What is the average number of friends do users have?
def Analysis_One():
    print(type(str_response))
    friends_sum = 0
    for i in range(int(count)):
        jsonData = tweets["statuses"][i]["user"]
    # print(tweets["statuses"][0]["user"].keys())
    # for item in jsonData:
        friends_count = jsonData["friends_count"]
        id = jsonData["id"]
        friends_sum += int(friends_count)
        print("User id is: {}".format(id), "  User friends_count is: {}".format(friends_count))
    friends_avg = friends_sum/int(count)
    print("Users' average friends count is: {}".format(friends_avg))

# #Analysis two: States; Find mode

def Analysis_Two():
    dic = {'Foreign': '0', 'Alien': '0', 'Alabama': '0', 'Alaska': '0', 'American Samoa': '0', 'Arizona': '0',
           'Arkansas': '0', 'California': '0', 'Colorado': '0', 'Connecticut': '0', 'Delaware': '0',
           'Washington, D.C.': '0', 'Florida': '0', 'Georgia': '0', 'Guam': '0', 'Hawaii': '0', 'Idaho': '0',
           'Illinois': '0', 'Indiana': '0', 'Kansas': '0', 'Iowa': '0', 'Kentucky': '0', 'Louisiana': '0', 'Maine': '0',
           'Maryland': '0', 'Marshall Islands': '0', 'Massachusetts': '0', 'Michigan': '0', 'Micronesia': '0',
           'Minnesota': '0', 'Mississippi': '0', 'Montana': '0', 'Nebraska': '0', 'Nevada': '0', 'New Hampshire': '0',
           'New Jersey': '0', 'New Mexico': '0', 'New York': '0', 'North Carolina': '0', 'North Dakota': '0',
           'Northern Marianas': '0', 'Ohio': '0', 'Oklahoma': '0', 'Oregon': '0', 'Palau': '0', 'Pennsylvania': '0',
           'Puerto Rico': '0', 'Rhode Island': '0', 'Missouri': '0', 'South Carolina': '0', 'South Dakota': '0',
           'Tennessee': '0', 'Texas': '0', 'Utah': '0', 'Vermont': '0', 'Virginia': '0', 'Virgin Islands': '0',
           'Washington': '0', 'West Virginia': '0', 'Wisconsin': '0', 'Wyoming': '0'}
    dic = dic.fromkeys(dic.keys(), 0)

    for i in range(int(count) - 1):
        jsonData = tweets["statuses"][i]["user"]
        user_location = jsonData["location"]
        id = jsonData["id"]

        url = "http://api.geonames.org/searchJSON?formatted=true&q=" + user_location + "&maxRows=10&lang=en&username=limuzi0609&style=full"
        data = json.dumps({"name": "test_repo", "description": "test"})
        r = requests.post(url, data)
        print(user_location)
        if r.json()["totalResultsCount"] == 0:
            dic['Alien'] += 1
        elif r.json()["geonames"][0]["countryCode"] == "US" and r.json()["geonames"][0]["adminName1"] is not '':
            state = r.json()["geonames"][0]["adminName1"]
            dic[state] += 1
        else:
            dic['Foreign'] += 1

    dic = {k: v for (k, v) in dic.items() if v > 0}
    print(dic.items())
    # visualisation
    wordlist=[]
    for key,val in dic.items():
        wordlist.append((key,val))
    matplotlib.pyplot.figure(figsize=(9, 6))
    wordlist.sort()
    keylist=[key for key,val in wordlist]
    vallist=[val for key,val in wordlist]
    barwidth=0.3
    xVal=np.arange(len(keylist))
    pylab.xticks(xVal+barwidth/2.0,keylist,rotation=45)
    pylab.bar(xVal,vallist,width=barwidth,color='lightskyblue',edgecolor = 'white')

    pylab.title(u"Bar Chart of Users' States" )
    pylab.show()

    # print("User id is: {}".format(id), "  User location is: " + user_location)
# print(tweets)

# Analysis Three: Relationship between retweets and followers number

def Analysis_Three():
    matplotlib.pyplot.figure(figsize=(9,6))

    followers_num = []
    retweet_num = []

    for i in range(int(count)):
        followers_count = tweets["statuses"][i]["user"]["followers_count"]
        retweet_count = tweets["statuses"][i]["retweet_count"]
        followers_num.append(followers_count)
        retweet_num.append(retweet_count)
        print("Tweets retweet number is: {}".format(retweet_count), " User's followers number is: {}".format(followers_count))

    T = np.arctan2(followers_num,retweet_num)
    matplotlib.pyplot.scatter(followers_num,retweet_num,c=T,s=25,alpha=0.4,marker='o')
    matplotlib.pyplot.xlabel("User's follower number")
    matplotlib.pyplot.ylabel("User's this tweet's retweet number")
    matplotlib.pyplot.show()

# Analysis Four: Average mention users' number
def Analysis_Four():
    user_mentioned = 0
    for i in range(int(count)):
        mentioned_count = len(tweets["statuses"][i]["entities"]["user_mentions"])
        id = tweets["statuses"][i]["user"]["id"]
        user_mentioned += mentioned_count
        print("User id is: {}".format(id), "  User mentioned people number is: {}".format(mentioned_count))
    mentioned_avg = user_mentioned/int(count)
    print("Users' average friends count is: {}".format(mentioned_avg))

# Analysis Five: Average mention users' number
def Analysis_Five():
    term_1 = input("What do you want to search?")
    if choose_time == 1:
        # global search_1
        integra_search = "%20since%3A" + date_0 + '&count=' + count
        search_2 = "https://api.twitter.com/1.1/search/tweets.json?q=" + term_1 + integra_search
    if choose_time == 2:
        # global search_1
        integra_search = "%20until%3A" + date_0 + '&count=' + count
        search_2 = "https://api.twitter.com/1.1/search/tweets.json?q=" + term_1 + integra_search
    else:
        search_2 = "https://api.twitter.com/1.1/search/tweets.json?q=" + term_1 + "%20until%3A" + date_0 + '&count=' + count
        print("Your input is wrong, please input again")

    response_1, data_1 = client.request(search_2)

    str_response_1 = data_1.decode('utf-8')
    tweets_1 = json.loads(str_response_1)

    dic = {'Foreign': '0', 'Alien': '0', 'Alabama': '0', 'Alaska': '0', 'American Samoa': '0', 'Arizona': '0',
           'Arkansas': '0', 'California': '0', 'Colorado': '0', 'Connecticut': '0', 'Delaware': '0',
           'Washington, D.C.': '0', 'Florida': '0', 'Georgia': '0', 'Guam': '0', 'Hawaii': '0', 'Idaho': '0',
           'Illinois': '0', 'Indiana': '0', 'Kansas': '0', 'Iowa': '0', 'Kentucky': '0', 'Louisiana': '0', 'Maine': '0',
           'Maryland': '0', 'Marshall Islands': '0', 'Massachusetts': '0', 'Michigan': '0', 'Micronesia': '0',
           'Minnesota': '0', 'Mississippi': '0', 'Montana': '0', 'Nebraska': '0', 'Nevada': '0', 'New Hampshire': '0',
           'New Jersey': '0', 'New Mexico': '0', 'New York': '0', 'North Carolina': '0', 'North Dakota': '0',
           'Northern Marianas': '0', 'Ohio': '0', 'Oklahoma': '0', 'Oregon': '0', 'Palau': '0', 'Pennsylvania': '0',
           'Puerto Rico': '0', 'Rhode Island': '0', 'Missouri': '0', 'South Carolina': '0', 'South Dakota': '0',
           'Tennessee': '0', 'Texas': '0', 'Utah': '0', 'Vermont': '0', 'Virginia': '0', 'Virgin Islands': '0',
           'Washington': '0', 'West Virginia': '0', 'Wisconsin': '0', 'Wyoming': '0'}
    dic_1 = {'Foreign': '0', 'Alien': '0', 'Alabama': '0', 'Alaska': '0', 'American Samoa': '0', 'Arizona': '0',
           'Arkansas': '0', 'California': '0', 'Colorado': '0', 'Connecticut': '0', 'Delaware': '0',
           'Washington, D.C.': '0', 'Florida': '0', 'Georgia': '0', 'Guam': '0', 'Hawaii': '0', 'Idaho': '0',
           'Illinois': '0', 'Indiana': '0', 'Kansas': '0', 'Iowa': '0', 'Kentucky': '0', 'Louisiana': '0', 'Maine': '0',
           'Maryland': '0', 'Marshall Islands': '0', 'Massachusetts': '0', 'Michigan': '0', 'Micronesia': '0',
           'Minnesota': '0', 'Mississippi': '0', 'Montana': '0', 'Nebraska': '0', 'Nevada': '0', 'New Hampshire': '0',
           'New Jersey': '0', 'New Mexico': '0', 'New York': '0', 'North Carolina': '0', 'North Dakota': '0',
           'Northern Marianas': '0', 'Ohio': '0', 'Oklahoma': '0', 'Oregon': '0', 'Palau': '0', 'Pennsylvania': '0',
           'Puerto Rico': '0', 'Rhode Island': '0', 'Missouri': '0', 'South Carolina': '0', 'South Dakota': '0',
           'Tennessee': '0', 'Texas': '0', 'Utah': '0', 'Vermont': '0', 'Virginia': '0', 'Virgin Islands': '0',
           'Washington': '0', 'West Virginia': '0', 'Wisconsin': '0', 'Wyoming': '0'}
    dic = dic.fromkeys(dic.keys(), 0)
    dic_1 = dic_1.fromkeys(dic_1.keys(), 0)

    for i in range(int(count) - 1):
        jsonData = tweets["statuses"][i]["user"]
        jsonData_1 = tweets_1["statuses"][i]["user"]
        user_location = jsonData["location"]
        user_location_1 = jsonData_1["location"]
        id = jsonData["id"]
        id_1 = jsonData_1["id"]

        url = "http://api.geonames.org/searchJSON?formatted=true&q=" + user_location + "&maxRows=10&lang=en&username=limuzi0609&style=full"
        url_1 = "http://api.geonames.org/searchJSON?formatted=true&q=" + user_location_1 + "&maxRows=10&lang=en&username=limuzi0609&style=full"
        data = json.dumps({"name": "test_repo", "description": "test"})
        data_1 = json.dumps({"name": "test_repo", "description": "test"})
        r = requests.post(url, data)
        r_1 = requests.post(url_1, data_1)
        print(user_location)
        print(user_location_1)
        if r.json()["totalResultsCount"] == 0:
            dic['Alien'] += 1
        elif r.json()["geonames"][0]["countryCode"] == "US" and r.json()["geonames"][0]["adminName1"] is not '':
            state = r.json()["geonames"][0]["adminName1"]
            dic[state] += 1
        else:
            dic['Foreign'] += 1

        if r_1.json()["totalResultsCount"] == 0:
            dic_1['Alien'] += 1
        elif r_1.json()["geonames"][0]["countryCode"] == "US" and r_1.json()["geonames"][0]["adminName1"] is not '':
            state_1 = r_1.json()["geonames"][0]["adminName1"]
            dic_1[state_1] += 1
        else:
            dic_1['Foreign'] += 1

    #dic = {k: v for (k, v) in dic.items() if v > 0}
    print(dic.items())
    #dic_1 = {k: v for (k, v) in dic_1.items() if v > 0}
    print(dic_1.items())
    # visualisation
    wordlist = []
    wordlist_1 = []
    for key, val in dic.items():
        wordlist.append((key, val))
    matplotlib.pyplot.figure(figsize=(9, 6))
    wordlist.sort()
    keylist = [key for key, val in wordlist]
    vallist = [val for key, val in wordlist]

    for key_1, val_1 in dic_1.items():
        wordlist_1.append((key_1, val_1))
    wordlist_1.sort()
    keylist_1 = [key_1 for key_1, val_1 in wordlist_1]
    vallist_1 = [val_1 for key_1, val_1 in wordlist_1]

    barwidth = 0.35
    xVal = np.arange(len(keylist))+1
    pylab.xticks((xVal*2 + barwidth) / 2.0, keylist, rotation=45)
    pylab.bar(xVal, vallist, width=barwidth, color='lightskyblue', edgecolor='white')
    pylab.bar(xVal+0.35, vallist_1, width=barwidth, color='yellowgreen', edgecolor='white')

    pylab.title(u"Lightskyblue for Trump, Yellowgreen for Clinton")
    pylab.show()

if __name__ == '__main__':
    Save_Json()
    Analysis_One()
    Analysis_Two()
    Analysis_Three()
    Analysis_Four()
    Analysis_Five()

    parser = ArgumentParser(description='Process some integers.')
    parser.add_argument('--1', default=Analysis_One(), help='Analysis 1')
    parser.add_argument('--2', default=Analysis_Two(), help='Analysis 2')
    parser.add_argument('--3', default=Analysis_Three(), help='Analysis 3')
    parser.add_argument('--4', default=Analysis_Four(), help='Analysis 4')
    parser.add_argument('--5', default=Analysis_Five(), help='Analysis 5')
    args = parser.parse_args()
    print(args.accumulate(args.integers))