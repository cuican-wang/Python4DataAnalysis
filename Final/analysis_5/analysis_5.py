import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import numpy as np

data = pd.read_csv('C:/Users/Wang/Desktop/Python4DataAnalysis/Final/data/webScrepedData.csv')
city = ['San-Francisco','Boston','Palo-Alto','Chicago','New-York','Washington','Seattle','Atlanta','Houston','San-Diego']
city_dict = dict.fromkeys(city, 0)
for n in range(len(data)):
    job_city = data.loc[n,'jobCity']
    city_dict[job_city] += 1

city_dict_frame = pd.DataFrame(list(city_dict.items()))
city_dict_frame.columns = ['city','number_of_jobs']
city_dict_frame = city_dict_frame.sort_values('number_of_jobs',ascending=True)

sns.set_style('whitegrid')
sns.set(font_scale=3)
fig, ax = plt.subplots()
# the size of A4 paper
fig.set_size_inches(30, 4.5)
fig = sns.barplot(x=city_dict_frame['city'], y=city_dict_frame['number_of_jobs'],data=city_dict_frame)
fig.figure.suptitle("Number of job posts for each city", fontsize = 40)
plt.ylabel('Number of job posts', fontsize=32)
plt.xlabel('City', fontsize=32)
for p,bar in zip(ax.patches,ax.patches):
    bar.set_width(0.5)
    ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))

plt.show()

city_day_dict = dict.fromkeys(city, 0)

for m in city:
    date_time = []
    for n in range(len(data)):
        if data.loc[n,"jobCity"] == m:
            # print('work')
            postdate_str = data.loc[n,'postDate'].split(':')[0][0:10]
            post_datetime = datetime.strptime(postdate_str, '%Y-%m-%d')
            # print("post_datetime"+post_datetime)
            date_time.append(post_datetime)
    # print("date_time")
    # print(date_time)
    maxdatetime = max(date_time)
    #print("maxdatetime:"+maxdatetime)
    mindatetime = min(date_time)
    days = (maxdatetime - mindatetime).days
    city_day_dict[m] = days

city_dict_frame['days'] = np.random.randn(len(city_dict_frame))
for m in range(len(city_dict_frame)):
    city_dict_frame.loc[m,'days'] = city_day_dict[city_dict_frame.loc[m,'city']]
city_dict_frame['frequency'] = np.random.randn(len(city_dict_frame))
for m in range(len(city_dict_frame)):
    city_dict_frame.loc[m,'frequency'] ="%.2f" % (city_dict_frame.loc[m,'number_of_jobs'] / city_dict_frame.loc[m,'days'])
for n in range(len(city_dict_frame)):
    city_dict_frame.loc[n,'frequency'] = float(city_dict_frame.loc[n,'frequency'])
city_dict_frame = city_dict_frame.sort_values('frequency',ascending = True)

sns.set_style('whitegrid')
sns.set(font_scale=3)
fig, ax = plt.subplots()
# the size of A4 paper
fig.set_size_inches(30, 4.5)
fig = sns.barplot(x=city_dict_frame['city'], y=city_dict_frame['frequency'],data=city_dict_frame)
fig.figure.suptitle("Job posts frequency for each city", fontsize = 40)
plt.ylabel('jobs/per day', fontsize=32)
plt.xlabel('City', fontsize=32)
for p,bar in zip(ax.patches,ax.patches):
    bar.set_width(0.5)
    ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))
sns.set(font_scale=3)
plt.show()