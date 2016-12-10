import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

#global data, scores,program_languages,analysis_software,bigdata_tool,databases,degree,overall,program_languages_score,analysis_software_score,bigdata_tool_score,databases_score,degree_score





def plotall(city,program_languages,analysis_software,bigdata_tool,databases,degree,program_languages_score,analysis_software_score,bigdata_tool_score,databases_score,degree_score):
    def plot_programming(city,program_languages,program_languages_score):
        colors = ['#FFC0CB', '#FF69B4', '#DB7093', '#FFA07A', '#FF7F50', '#FFA500', '#FFD700', '#F0E68C', '#E6E6FA',
                  '#DDA0DD',
                  '#9370DB', '#ADFF2F']
        explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)  # explode 1st slice
        font = {'family': 'Bitstream Vera Sans',
                'weight': 'bold',
                'size': 40}

        matplotlib.rc('font', **font)
        # Plot
        plt.pie(program_languages_score, explode=explode, labels=program_languages, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=200)
        plt.suptitle(city + " programming language needed pie chart", fontsize=60)
        plt.axis('equal')
        plt.show()
    plot_programming(city,program_languages,program_languages_score)

    def plot_analysis(city,analysis_software,analysis_software_score):
        colors = ['#FFC0CB', '#FF69B4', '#DB7093', '#FFA07A', '#FF7F50', '#FFA500', '#FFD700', '#F0E68C', '#E6E6FA',
                  '#DDA0DD', '#9370DB', '#ADFF2F', '#00FF7F', '#9ACD32', '#66CDAA', '#00FFFF', '#00BFFF']
        explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)  # explode 1st slice
        font = {'family': 'Bitstream Vera Sans',
                'weight': 'bold',
                'size': 40}

        matplotlib.rc('font', **font)
        # Plot
        plt.pie(analysis_software_score, explode=explode, labels=analysis_software, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=200)
        plt.suptitle(city+" analysis software needed pie chart", fontsize=60)
        plt.axis('equal')
        plt.show()
    plot_analysis(city,analysis_software,analysis_software_score)

    def plot_bigdata(city,bigdata_tool,bigdata_tool_score):
        colors = ['#FFC0CB', '#FF69B4', '#DB7093', '#FFA07A', '#FF7F50', '#FFA500', '#FFD700', '#F0E68C', '#E6E6FA',
                  '#DDA0DD', '#9370DB']
        explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)  # explode 1st slice
        font = {'family': 'Bitstream Vera Sans',
                'weight': 'bold',
                'size': 40}

        matplotlib.rc('font', **font)
        # Plot
        plt.pie(bigdata_tool_score, explode=explode, labels=bigdata_tool, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=200)
        plt.suptitle(city+" bigdata tools needed pie chart", fontsize=60)
        plt.axis('equal')
        plt.show()
    plot_bigdata(city,bigdata_tool,bigdata_tool_score)

    def plot_database(city,databases,databases_score):
        colors = ['#FFC0CB', '#FF69B4', '#DB7093', '#FFA07A', '#FF7F50', '#FFA500', '#FFD700', '#F0E68C', '#E6E6FA',
                  '#DDA0DD']
        explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0)  # explode 1st slice
        font = {'family': 'Bitstream Vera Sans',
                'weight': 'bold',
                'size': 40}

        matplotlib.rc('font', **font)
        # Plot
        plt.pie(databases_score, explode=explode, labels=databases, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=200)
        plt.suptitle(city+" database skills needed pie chart", fontsize=60)
        plt.axis('equal')
        plt.show()
    plot_database(city,databases,databases_score)

    def plot_degree(city,degree,degree_score):
        colors = ['#FFC0CB', '#FFA07A', '#DDA0DD']
        explode = (0.1, 0, 0)  # explode 1st slice
        font = {'family': 'Bitstream Vera Sans',
                'weight': 'bold',
                'size': 40}

        matplotlib.rc('font', **font)
        # Plot
        plt.pie(degree_score, explode=explode, labels=degree, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=200)
        plt.suptitle(city+" degree needed pie chart", fontsize=60)
        plt.axis('equal')
        plt.show()
    plot_degree(city,degree,degree_score)

#plotall(city,program_languages_score,analysis_software_score,bigdata_tool_score,databases_score,degree_score)

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

    city = input("For which city do you want to see: ")

    if city == 'Overall':
        plot_data = data
    else:
        plot_data = pd.DataFrame(columns=data.columns)
        for n in range(len(data)):
            if data.loc[n, 'jobCity'] == city:
                plot_data.loc[n] = data.loc[n]

    plot_data.index = range(len(plot_data))

    for m in range(len(overall)):
        for n in overall[m]:
            score = 0
            for i in range(len(plot_data)):
                score += plot_data.loc[i, n]
            scores[m].append(score)
    plotall(city, program_languages, analysis_software, bigdata_tool, databases, degree, program_languages_score, analysis_software_score, bigdata_tool_score, databases_score, degree_score)