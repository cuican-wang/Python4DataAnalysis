# import requests,json
#
# url = "http://api.geonames.org/searchJSON?formatted=true&q=boston&maxRows=10&lang=es&username=limuzi0609&style=full"
# data = json.dumps({"name":"test_repo","description":"test"})
# r = requests.post(url,data)
# print(r.json()["geonames"][0]["adminName1"])

# for i in range(2):
#     print(i)

# dic = {'Foreign':'0','Alien':'0','Alabama':'0','Alaska':'0','American Samoa':'0','Arizona':'0','Arkansas':'0','California':'0','Colorado':'0','Connecticut':'0','Delaware':'0','Washington, D.C.':'0','Florida':'0','Georgia':'0','Guam':'0','Hawaii':'0','Idaho':'0','Illinois':'0','Indiana':'0','Kansas':'0','Iowa':'0','Kentucky':'0','Louisiana':'0','Maine':'0','Maryland':'0','Marshall Islands':'0','Massachusetts':'0','Michigan':'0','Micronesia':'0','Minnesota':'0','Mississippi':'0','Montana':'0','Nebraska':'0','Nevada':'0','New Hampshire':'0','New Jersey':'0','New Mexico':'0','New York':'0','North Carolina':'0','North Dakota':'0','Northern Marianas':'0','Ohio':'0','Oklahoma':'0','Oregon':'0','Palau':'0','Pennsylvania':'0','Puerto Rico':'0','Rhode Island':'0','Missouri':'0','South Carolina':'0','South Dakota':'0','Tennessee':'0','Texas':'0','Utah':'0','Vermont':'0','Virginia':'0','Virgin Islands':'0','Washington':'0','West Virginia':'0','Wisconsin':'0','Wyoming':'0'}
# dic = dic.fromkeys(dic.keys(),0)
# print(dic.items())

# import argparse
#
# parser = argparse.ArgumentParser(description='Process some integers.')
# parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                     help='an integer for the accumulator')
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                     help='sum the integers (default: find the max)')
#
# args = parser.parse_args()
# print(args.accumulate(args.integers))

ee = 'cc'
cc = 'ee'
print(ee)
print(cc)