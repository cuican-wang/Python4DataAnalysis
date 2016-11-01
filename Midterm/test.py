# hours = input("Input hours:")
# rate = input("rate: ")
# try:
#     hours = int(hours)
#     rate = int(rate)
# except:
#     print("Error, please input numeric input")
#     quit()
# print("Income = ")

# score = input("Enter Score: ")
# try:
#     s = float(score)
#     if s >= 0.0 and s <= 1.0:
#         if s >=0.9:
#             print ("A")
#         elif s >= 0.8:
#             print ("B")
#         elif s >= 0.7:
#             print ("C")
#         elif s >= 0.6:
#             print ("D")
#         else:
#             print ("F")
#     else:
#         print ("errorA")
# except:
#     print ("errorB")
#     quit()

# def stuff():
#     # print( 'Hello')
#     return
#     print( 'World')
#
# stuff()

import requests,json
import datetime,time
# def inputp():
#     global page,pagesize,fromdate,todate
#     page = input("Please input page number: ")
#     pagesize = input("Please input pagesize: ")
#     fromdate = input("Please input fromdate in format \"year-month-day\": ")
#     todate = input("Please input todate in format \"year-month-day\": ")
# inputp()
# # try:
# p = int(page)
# ps = int(pagesize)
# fd = int(datetime.datetime.strptime(fromdate, "%Y-%m-%d").timestamp())
# td = int(datetime.datetime.strptime(todate, "%Y-%m-%d").timestamp())
# # except:
# #     print("Error! Please input an integer")
# #     inputp()
# print(p,ps,fd,td)
# list = []
# print(type(list))
# import calendar
# print(str(int(datetime.datetime.today().timestamp())))
# class Solution(object):
#     def fizzBuzz(self, n):
#         l = list(range(1,n+1))
#         for i in range(n):
#             if l[i]%3==0 and l[i]%5==0:
#                 l[i]="FizzBuzz"
#             elif l[i]%3==0 and not l[i]%5==0:
#                 l[i]="Fizz"
#             elif l[i]%5==0 and not l[i]%3==0:
#                 l[i]="Buzz"
#             else:
#                 l[i]=str(l[i])
#         return l
# badge_c = [61, 1, 14, 1, 2, 9, 1, 5, 6, 12]
# sorted(range(len(badge_c)), key=lambda i: badge_c[i])[-2:]
# print(key)
# ps = 5
# dct = {}
# for i in range(ps):
#     dct['lst_%s' % i] = []
#     dct['lst_%s' % i].append(1)
#     dct['lst_%s' % i].append(2)
# print(dct)

# url_2 = "https://api.stackexchange.com/2.2/users/2320577/tags?page=1&pagesize=99&fromdate=0&todate=1477872000&order=desc&sort=popular&site=stackoverflow&key=V2ppRMfH*kBE7Wxr4D0kCg(("
# data_2 = json.dumps({"name": "test_repo", "description": "test"})
# r_2 = requests.get(url_2, data_2)
# print((len(r_2.json()["items"])))
dic = {1:[1,2,3,4,5]}
list = []
list.extend(dic[1][1:])
print(list)