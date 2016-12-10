import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from analysis_2.analysis_2 import plotall


# data = preparation().data


# large_company_number = 0
# medium_company_number = 0
# small_company_number = 0
#
# for n in range(len(data)):
#     if data.loc[n,'cmpEmployees'] in ['501 to 1,000', '1,001 to 5,000', '5,001 to 10,000', '10,000+']:
#         large_company_number += 1
#     elif data.loc[n,'cmpEmployees'] in ['51 to 200', '201 to 500']:
#         medium_company_number += 1
#     else:
#         small_company_number += 1
# print('large_company_number: ' + str(large_company_number))
# print('medium_company_number: ' + str(medium_company_number))
# print('small_company_number: ' + str(small_company_number))


def inputcmp():
    global company,employees
    company = input("For which kind of company do you want to see: ")
    if company == 'large company':
        employees = ['501 to 1,000', '1,001 to 5,000', '5,001 to 10,000', '10,000+']
    elif company == 'medium company':
        employees = ['51 to 200', '201 to 500']
    elif company == 'small company':
        employees = ['NA', '2 to 10', '11 to 50']
    else:
        print("Please choose one from [large company,medium company,small company] to input ")
        inputcmp()

if __name__ == "__main__":

    data = pd.read_csv('C:/Users/Wang/Desktop/Python4DataAnalysis/Final/data/webScrepedData.csv')

    program_languages = ['bash', 'r', 'python', 'java', 'c++', 'ruby', 'perl', 'javascript', 'scala', 'php', 'c',
                         'shell']
    analysis_software = ['matlab', 'excel', 'tableau', 'd3.js', 'sas', 'spss', 'd3', 'saas', 'pandas', 'numpy', 'scipy',
                         'sps', 'spotfire', 'scikits.learn', 'splunk', 'powerpoint', 'h2o']
    bigdata_tool = ['linux', 'hadoop', 'mapreduce', 'spark', 'pig', 'hive', 'shark', 'oozie', 'zookeeper', 'flume',
                    'mahout']
    databases = ['sql', 'nosql', 'hbase', 'cassandra', 'mongodb', 'mysql', 'mssql', 'postgresql', 'oracle', 'rdbms']
    degree = ["master", "ph.d", "bachelor"]
    overall = [program_languages, analysis_software, bigdata_tool, databases, degree]

    program_languages_score = []
    analysis_software_score = []
    bigdata_tool_score = []
    databases_score = []
    degree_score = []
    scores = [program_languages_score, analysis_software_score, bigdata_tool_score, databases_score, degree_score]

    inputcmp()
    plot_data = pd.DataFrame(columns=data.columns)
    for n in range(len(data)):
        if data.loc[n, 'cmpEmployees'] in employees:
            plot_data.loc[n] = data.loc[n]
    plot_data.index = range(len(plot_data))

    for m in range(len(overall)):
        for n in overall[m]:
            score = 0
            for i in range(len(plot_data)):
                score += plot_data.loc[i, n]
            scores[m].append(score)
    plotall(company, program_languages,analysis_software,bigdata_tool,databases,degree,program_languages_score, analysis_software_score, bigdata_tool_score, databases_score, degree_score)