import pandas as pd
import os

data = pd.read_csv('C:/Users/Wang/Desktop/Python4DataAnalysis/Final/data/webScrepedData.csv')

data_boston = pd.DataFrame(columns = data.columns)
data_sanfran = pd.DataFrame(columns = data.columns)
data_houston = pd.DataFrame(columns = data.columns)
data_chicago = pd.DataFrame(columns = data.columns)
data_palo = pd.DataFrame(columns = data.columns)
data_newyork = pd.DataFrame(columns = data.columns)
data_seattle = pd.DataFrame(columns = data.columns)
data_dc = pd.DataFrame(columns = data.columns)
data_atlanta = pd.DataFrame(columns = data.columns)
data_sandiego = pd.DataFrame(columns = data.columns)

for n in range(len(data)):
    if data.iloc[n]['jobCity'] == 'Atlanta':
        data_atlanta.loc[n] = data.iloc[n]
    elif data.iloc[n]['jobCity'] == 'Boston':
        data_boston.loc[n] = data.iloc[n]
    elif data.iloc[n]['jobCity'] == 'Chicago':
        data_chicago.loc[n] = data.iloc[n]
    elif data.iloc[n]['jobCity'] == 'Houston':
        data_houston.loc[n] = data.iloc[n]
    elif data.iloc[n]['jobCity'] == 'New-York':
        data_newyork.loc[n] = data.iloc[n]
    elif data.iloc[n]['jobCity'] == 'Palo-Alto':
        data_palo.loc[n] = data.iloc[n]
    elif data.iloc[n]['jobCity'] == 'San-Diego':
        data_sandiego.loc[n] = data.iloc[n]
    elif data.iloc[n]['jobCity'] == 'San-Francisco':
        data_sanfran.loc[n] = data.iloc[n]
    elif data.iloc[n]['jobCity'] == 'Seattle':
        data_seattle.loc[n] = data.iloc[n]
    elif data.iloc[n]['jobCity'] == 'Washington':
        data_dc.loc[n] = data.iloc[n]

def ensure_dir(f):
    if not os.path.exists(f):
        os.makedirs(f)

data_all = [data_atlanta,data_boston,data_chicago,data_houston,data_newyork,data_palo,data_sandiego,data_sanfran,data_seattle,data_dc]
city = ['Atlanta','Boston','Chicago','Houston','New-York','Palo-Alto','San-Diego','San-Francisco','Seattle','Washington']

# create subfolders by cities
for n in range(len(data_all)):
    data_all[n].index = range(len(data_all[n]))
    path = 'C:/Users/Wang/Desktop/Python4DataAnalysis/Final/data/'
    folderpath = path + city[n]
    ensure_dir(folderpath)
    csvpath = folderpath + '/' + city[n] + '.csv'
    data_all[n].to_csv(csvpath, encoding='utf-8')

# create subfolders by post date
for n in range(len(data_all)):
    basepath = 'C:/Users/Wang/Desktop/Python4DataAnalysis/Final/data/'+city[n] + '/'
    for m in data_all[n].postDate.unique():
        folderpath = basepath + m.split(':')[0][:-3]
        ensure_dir(folderpath)
        a = pd.DataFrame(columns=data.columns)
        for i in range(len(data_all[n])):
            if data_all[n].iloc[i].postDate == m:
                a.loc[i] = data_all[n].iloc[i]
                csvpath = folderpath + '/' + m.split(':')[0][:-3] + '.csv'
                a.to_csv(csvpath,encoding='utf-8')