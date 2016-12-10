import pandas as pd
import indicoio
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

if not os.path.exists('C:/Users/Wang/Desktop/Python4DataAnalysis/Final/analysis_1/sortedScore.csv'):
    data = pd.read_csv('C:/Users/Wang/Desktop/Python4DataAnalysis/Final/data/webScrepedData.csv')
    data_copy = data
    # remove duplicate rows
    data_copy = data_copy.drop_duplicates(subset=['jobCity','cmpReviews'],keep = False)
    data_copy.index = range(len(data_copy))
    cmpData = pd.DataFrame(columns = data_copy.columns)
    # remove rows with reviews characters less than 4000
    for n in range(len(data_copy)):
        if len(data_copy.loc[n]['cmpReviews']) > 4000:
            cmpData.loc[n] = data_copy.loc[n]
    cmpData.index = range(len(cmpData))
    del cmpData['Unnamed: 0']

    indicoio.config.api_key = 'c6ef58328ddb406eb8f61ea9012d28ae'

    cmp_overall = cmpData
    cmp_overall['reviewScore'] = np.random.randn(len(cmp_overall))
    for n in range(len(cmpData)):
        cmp_overall.loc[n,'reviewScore']= indicoio.sentiment_hq(cmpData.loc[n,'cmpReviews'])
    for n in range(len(cmp_overall)):
        cmp_overall.loc[n,'reviewScore'] = "%.2f" % (cmp_overall.loc[n,'reviewScore'] * 100)
    for n in range(len(cmp_overall)):
        cmp_overall.loc[n,'reviewScore'] = float(cmp_overall.loc[n,'reviewScore'])
    cmp_overall.sort_values(['reviewScore'],ascending=False,inplace=True)
    cmp_overall.index = range(len(cmp_overall))
    cmp_overall.to_csv('C:/Users/Wang/Desktop/Python4DataAnalysis/Final/analysis_1/sortedScore.csv',encoding='utf-8')
else:
    cmp_overall = pd.read_csv('C:/Users/Wang/Desktop/Python4DataAnalysis/Final/analysis_1/sortedScore.csv')

def plot_rank(number,city):
    number = int(number)
    if city == 'Overall':
        rank_data = cmp_overall
    else:
        rank_data = pd.DataFrame(columns=cmp_overall.columns)
        for n in range(len(cmp_overall)):
            if cmp_overall.loc[n,'jobCity'] == city:
                rank_data.loc[n] = cmp_overall.loc[n]

    rank_data.index = range(len(rank_data))
    rank_data_top = rank_data[:number]
    rank_data_last = rank_data[-number:]
    rank_data_plot = pd.concat([rank_data_top,rank_data_last])
    rank_data_plot.index = range(len(rank_data_plot))
    rank_data_plot.head()
    # rank_data_top.index = range(len(rank_data_top))
    # rank_data_last.index = range(len(rank_data_last))

    sns.set_style('whitegrid')
    sns.set(font_scale=3)
    fig, ax = plt.subplots()
    # the size of A4 paper
    fig.set_size_inches(30, 3)
    fig = sns.barplot(x="cmpName", y="reviewScore", data=rank_data_plot)
    for item in fig.get_xticklabels():
        item.set_rotation(45)
    fig.figure.suptitle(city + " companies with review score in top 6 and last 6", fontsize=60)
    plt.ylabel('Score', fontsize=40)
    plt.xlabel('Company Name', fontsize=40)
    for p, bar in zip(ax.patches, ax.patches):
        bar.set_width(0.5)
        ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))
    ax.set(ylim=(0, 120))
    #fig.figure.get_axes()[0].set_yscale('log')
    plt.show()


number = input("How many companies do you want to see both in top and last as for the review scores: ")
city = input("For which city do you want to see: ")
plot_rank(number,city)