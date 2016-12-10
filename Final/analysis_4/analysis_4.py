import pandas as pd
from datetime import datetime
import calendar
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('C:/Users/Wang/Desktop/Python4DataAnalysis/Final/data/webScrepedData.csv')
perioddata = pd.DataFrame(columns = data.columns)

startdate = input('Input the start date(recommend 2016-10-17):')
enddate = input('Input the end date(recommend 2016-11-13):')

startdatetime = datetime.strptime(startdate,'%Y-%m-%d')
enddatetime = datetime.strptime(enddate,'%Y-%m-%d')

for n in range(len(data)):
    postDate = datetime.strptime(data.loc[n,'postDate'].split(':')[0][0:10],'%Y-%m-%d')
    if startdatetime <= postDate <= enddatetime:
        perioddata.loc[n] = data.loc[n]
perioddata.index = range(len(perioddata))

dict = {'Monday':0,'Tuesday':0,'Wednesday':0,'Thursday':0,'Friday':0,'Saturday':0,'Sunday':0}

for n in range(len(perioddata)):
    date = data.loc[n,'postDate'].split(':')[0][0:10]
    weekday = calendar.day_name[datetime.strptime(date, '%Y-%m-%d').weekday()]
    dict[weekday] += 1

dictframe = pd.DataFrame(list(dict.items()))

sns.set_style('whitegrid')
sns.set(font_scale=3)
fig, ax = plt.subplots()
# the size of A4 paper
fig.set_size_inches(30, 4.5)
fig = sns.barplot(x=dictframe[0], y=dictframe[1],data=dictframe)
fig.figure.suptitle("Job posts from "+ startdate +" to " + enddate, fontsize = 40)
plt.ylabel('Number of jobs', fontsize=32)
plt.xlabel(' ', fontsize=32)
# plt.xlabel('company name', fontsize=16)
for p,bar in zip(ax.patches,ax.patches):
    bar.set_width(0.5)
    ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))
plt.show()