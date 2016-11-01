import requests,json,csv
import datetime
from collections import Counter

def inputp():
    global page,pagesize,fromdate,todate,topic,p,ps,fd,td
    topic = input("Please input a topic you want to search: ")
    page = input("Please input page number: ")
    pagesize = input("Please input pagesize: ")
    fromdate = input("Please input fromdate in format \"year-month-day\": ")
    todate = input("Please input todate in format \"year-month-day\": ")

    try:
        p = int(page)
        ps = int(pagesize)
        fd = int(datetime.datetime.strptime(fromdate, "%Y-%m-%d").timestamp())
        td = int(datetime.datetime.strptime(todate, "%Y-%m-%d").timestamp())
    except:
        print("Error! Please input an integer or right format date ")
        inputp()
inputp()


# Analysis 1
def analysisOne(topic):
    global url,data,r
    url = "https://api.stackexchange.com/2.2/questions?page="+str(p)+"&pagesize="+str(ps)+"&fromdate="+str(fd)+"&todate="+str(td)+"&order=desc&sort=activity&tagged="+topic+"&site=stackoverflow&key=V2ppRMfH*kBE7Wxr4D0kCg(("
    data = json.dumps({"name":"test_repo","description":"test"})
    r = requests.get(url,data)

    #print(r.json())
    global list_q, list_id ,badge_c
    list_q = []
    list_id = []
    badge_c = []
    #t = str(int(datetime.datetime.today().timestamp()))
    for i in range(ps):
        problem = r.json()["items"][i]["title"]
        user_id = r.json()["items"][i]["owner"]["user_id"]
        print(user_id)
        list_q.append(problem)
        list_id.append(user_id)

        url_b = "https://api.stackexchange.com/2.2/users/"+str(user_id)+"/badges?page=1&pagesize=100&fromdate=0&todate="+str(td)+"&order=desc&sort=rank&site=stackoverflow&key=V2ppRMfH*kBE7Wxr4D0kCg(("
        data_b = json.dumps({"name":"test_repo","description":"test"})
        r_b = requests.get(url_b,data_b)
        badge_num = len(r_b.json()["items"])
        # print(badge_num)
        badge_c.append(badge_num)
    #print(badge_c)

    # Print the top 3 questions by sorting list and get the index
    print("The top 3 questions with user's badges number are: \n",sorted(zip(badge_c, list_q), reverse=True)[:3])
    list_1 = sorted(zip(badge_c, list_q), reverse=True)[:3]
    with open('analysisOne.csv', 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(list_1)


analysisOne(topic=topic)

# inputp()
# analysisOne(topic=topic)

# Analysis 2
# this function is to check how many tags does the user have then can know the page and pagesize

def analysisTwo_1():
    x = list(range(ps))
    global dct
    dct = {}

    for i in range(ps):
        dct['lst_%s' % list_id[i]] = []
        dct['lst_%s' % list_id[i]].append(list_id[i])
        for n in range(1,1000):
            url_2 = "https://api.stackexchange.com/2.2/users/" + str(list_id[i]) + "/tags?page=" + str(
                n) + "&pagesize=100&fromdate=0&todate=" + str(
                td) + "&order=desc&sort=popular&site=stackoverflow&key=V2ppRMfH*kBE7Wxr4D0kCg(("
            data_2 = json.dumps({"name": "test_repo", "description": "test"})
            r_2 = requests.get(url_2, data_2)
            if len(r_2.json()["items"]) == 0:
                break
            for m in range(100):
                try:
                    dct['lst_%s' % list_id[i]].append(r_2.json()["items"][m]["name"])
                except:
                    break
        print(dct)
        with open('analysisTwo_1.csv', 'w') as myfile:
            wr = csv.DictWriter(myfile, dct.keys())
            wr.writeheader()
            wr.writerow(dct)
analysisTwo_1()

def analysisTwo_2(filename,*keys):
    list_at2 = []
    # k = re.compile('["owner"].*\.')
    for i in range(ps):
        list_at2a = []
        for key in keys:
            if key=="score":

                list_at2a.append(r.json()["items"][i][key])
            else:
                list_at2a.append(r.json()["items"][i]["owner"][key])


        list_at2.extend([list_at2a])
    list_at2.sort(key=lambda x:x[len(keys)-1], reverse=True)
    # print(list_at2)
    with open(filename, 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(list_at2)
analysisTwo_2('analysisTwo_2.csv',"user_id","display_name","link","reputation")

def analysisThree():
    list_allB = []
    for i in range(ps):
        list_allB.extend(dct['lst_%s' % list_id[i]][1:])
    # print(list_allB)
    list_badges = Counter(list_allB)
    print(list_badges)
    with open('analysisThree.csv', 'w') as csvfile:
        # fieldnames = ['badges','count']
        writer = csv.writer(csvfile)
        # writer.writerow(fieldnames)
        for key, count in list_badges.items():
            badge = key
            writer.writerow([badge, count])
analysisThree()

def analysisFour(a,key,filename):

    dct_4 = {}
    for i in range(ps):
        dct_4['lst_%s' % a[i]] = []
        dct_4['lst_%s' % a[i]].append(a[i])
        if len(r.json()["items"]) == 0:
            break

        try:
            dct_4['lst_%s' % a[i]].append(r.json()["items"][i][key])
        except:
            break
        print(dct_4)
        with open(filename, 'w') as myfile:
            wr = csv.DictWriter(myfile, dct_4.keys())
            # wr.writeheader()
            wr.writerow(dct_4)

analysisFour(list_q,"tags",'analysisFour.csv')

# Analysis 5: Found out the user whose questions have been upvoted the most
analysisTwo_2('analysisFive.csv',"user_id","display_name","link","score")