# INFO7374 18218 Data Analysis Using Python - Fall 2016 #
## Final Project - Exploration of Data Scientist Jobs ##
This project is mainly about Data Scientist Jobs:

![](http://i.imgur.com/MnjD6Ti.jpg)

In order to solve the following problems:

1. How are skill-sets and degree needed among different city?
2. How are skill-sets and degree needed among different size of companies?
3. What about everyone's comments on the company?
4. Which day of a week does HR usually post jobs?
5. How is the distribution of job postings among these ten cities? what's the frequency of job posting for each city? 

## Collect Data ##
Data is web scraped and integrated from both Monster.com and Indeed.com among ten cities(San-Francisco, Boston, Palo Alto, Chicago, New-York, Washington, Seattle, Atlanta, Houston, San-Diego) including 5392 rows and 65 columns.


The first row of data I got is as following:

<div style="overflow-x: auto; overflow-y: auto; height: 250px; width:1000px;" type = "text/css">
    <table id="table" class="table" border="1" align="center" width="100px" height="200px">
  <tbody >
   <tr><th></th><th>jobTitle</th><th>cmpName</th><th>cmpRating</th><th>cmpReviewsAmount</th><th>cmpReviews</th><th>cmpEmployees
</th><th>jobCity
</th><th>jobRegion
</th><th>jobState
</th><th>postDate
</th><th>job_url
</th><th>bachelor
</th><th>bash</th><th>c</th><th>c++
</th><th>cassandra
</th><th>d3
</th><th>d3.js

</th><th>excel

</th><th>flume

</th><th>h2o

</th><th>hadoop

</th><th>hbase

</th><th>hive

</th><th>java
</th><th>javascript</th><th>linux</th><th>mahout</th><th>mapreduce</th><th>master
</th><th>matlab

</th><th>mongodb

</th><th>mssql

</th><th>mysql

</th><th>nosql

</th><th>numpy

</th><th>oozie
</th><th>oracle
</th><th>pandas

</th><th>perl

</th><th>ph.d

</th><th>php


</th><th>pig


</th><th>postgresql


</th><th>powerpoint


</th><th>python


</th><th>r


</th><th>rdbms


</th><th>ruby
</th><th>saas
</th><th>sas
</th><th>scala
</th><th>scikits.learn
</th><th>scipy

</th><th>shark

</th><th>shell

</th><th>spark

</th><th>splunk

</th><th>spotfire

</th><th>sps

</th><th>spss
</th><th>sql
</th><th>tableau

</th><th>zookeeper

</th></tr>
   <tr><td>1</td><td>Data Scientist - growth, marketing research - San Fran!
</td><td>CyberCoders
</td><td>3.5
</td><td>18
</td><td>As a selection representative you figure out how to construct your business starting with no...</td>
<td>NA</td>
<td>San-Francisco
</td><td>San Francisco
</td><td>CA
</td><td>2016-12-01T12:00
</td><td>http://jobview.monster.com/data-scientist-growth-marketing-research-san-fran!-job-san-francisco-ca-us-176931443.aspx?mescoid=1500152001001&jobPosition=1
</td><td>0
</td><td>0
</td><td>0
</td><td>0
</td><td>0
</td><td>0
</td><td>0
</td><td>0
</td><td>0
</td><td>0
</td><td>1
</td><td>0
</td><td>1
</td><td>0
</td><td>0
</td><td>0
</td><td>0
</td><td>0
</td><td>1
</td><td>0
</td><td>0
</td><td>0
</td><td>0
</td><td>0
</td><td>0
</td><td>0
</td><td>0
</td><td>0
</td><td>0
</td><td>0
</td><td>0
</td><td>1
</td><td>0
</td><td>0
</td><td>1
</td><td>1
</td><td>0
</td><td>0
</td><td>0
</td><td>0
</td><td>0
</td><td>0
</td><td>0
</td><td>0
</td><td>0
</td><td>0
</td><td>0
</td><td>0
</td><td>0
</td><td>0
</td><td>1
</td><td>0
</td><td>0
</td></tr>
</tbody>
  
</table>
</div>


## Data Pre-exploration: ##
Break down the whole data according to city and job post date. After pre-exploration, data is as following:

![](http://i.imgur.com/zMbZs8a.png)
![](http://i.imgur.com/lsddBO0.png)
![](http://i.imgur.com/q7lU3qh.png)
![](http://i.imgur.com/26K8yeq.png)

## Analysis_1: What about everyone's comments on the company?##
Performed sentiment analysis of companies' reviews and got a review score by using indicoio api.

        for n in range(len(cmpData)):
        cmp_overall.loc[n,'reviewScore']= indicoio.sentiment_hq(cmpData.loc[n,'cmpReviews'])

Higher score means more positive and lower score mean more negative. Analysis is dynamic, you can input city name and number of companies with Top and Last score. Part of the results are as following:
### Overall city review score rank(top 6 and last 6): ###

<div style="overflow-x: auto; overflow-y: auto; height: 250px; width:1000px;" type = "text/css">
    <table id="table" class="table" border="1" align="center" width="100px" height="200px">
  <tbody >
   <tr><th></th><th>jobTitle</th><th>cmpName</th><th>cmpRating</th><th>reviewScore</th></tr>

<tr><td>0</td><td>Data Scientist (People Analytics)</td><td>Genentech
</td><td>4.1
</td><td>99.96
</td></tr>

<tr><td>1
</td><td>Data Scientist
</td><td>Enterprise Solution inc
</td><td>4
</td><td>99.95
</td></tr>

<tr><td>2</td><td>Research Statistician
</td><td>Roche

</td><td>4.2
</td><td>99.93
</td></tr>

<tr><td>3</td><td>Lead Data Scientist in Machine Learning and Artificial Intelligence Tech College
</td><td>Capital One

</td><td>3.9

</td><td>99.93
</td></tr>

<tr><td>4</td><td>Data Scientist

</td><td>National Grid

</td><td>4.1
</td><td>99.92
</td></tr>

<tr><td>5</td><td>Data Warehouse Developer-Enterprise Analytics (40 HR, Days)
</td><td>Boston Medical Center

</td><td>4
</td><td>99.92
</td></tr>

<tr><td>6</td><td>Senior Biostatistician

</td><td>Cyberonics

</td><td>2.8

</td><td>5.62
</td></tr>

<tr><td>7
</td><td>Data Scientist
</td><td>Xerox

</td><td>3.4
</td><td>5.47
</td></tr>

<tr><td>8</td><td>Lead Data Scientist

</td><td>GrubHub


</td><td>3

</td><td>4.93

</td></tr>

<tr><td>9</td><td>Senior Public Health Scientists - Senior Project Managers
</td><td>ICF


</td><td>3.4


</td><td>4.68

</td></tr>

<tr><td>10</td><td>Data Scientist

</td><td>Stitch Fix


</td><td>3.3

</td><td>2.82

</td></tr>

<tr><td>11</td><td>Data Scientist
</td><td>Dupage Medical Group


</td><td>3

</td><td>0.45
</td></tr>

</tbody>
</table>
</div>
![Overall](http://i.imgur.com/jOvtZLk.png)
![Palo-Alto](http://i.imgur.com/3WKJxmw.png)
![Seattle](http://i.imgur.com/UWDlw3r.png)
![Boston](http://i.imgur.com/JBrlwkn.png)

## Analysis_2: How are skill-sets and degree needed among different city? ##
Performed analysis on skill-sets and degree mentioned in different job description among ten cities. You can input the city name you are interested in.

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

**Over all cities:**
![](http://i.imgur.com/0ERregd.png)
![](http://i.imgur.com/nl12xnr.png)
![](http://i.imgur.com/wKss9BL.png)
![](http://i.imgur.com/We6rI8Q.png)
![](http://i.imgur.com/ZBctxyA.png)

## Analysis_3: How are skill-sets and degree needed among different size of companies? ##
Performed analysis on skill-sets and degree mentioned in different job description among large,medium and small companies (divided by number of employees). You can input the kind of company you are interested in.

**Large companies:**
![](http://i.imgur.com/nkXeF8A.png)
![](http://i.imgur.com/lmd6B8G.png)
![](http://i.imgur.com/b1HWZIw.png)
![](http://i.imgur.com/8Shg1so.png)
![](http://i.imgur.com/ezzEVPE.png)

## Analysis_4: Which day of a week does HR usually post jobs? ##
Performed analysis on which day of a week usually have the most job postings. You can input the time period but I recommend the period as from 2016-10-17 to 2016-11-13 due to there are no holidays and timeliness factor.

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


<div style="overflow-x: auto; overflow-y: auto; height: 350px; width:300px;" type = "text/css">
    <table id="table" class="table" border="1" align="center" width="100px" height="200px">
  <tbody >
<tr><th></th><th>Day</th><th>Numbers</th></tr>
<tr><td>0</td><td>Monday</td><td>211</td></tr>
<tr><td>1</td><td>Sunday</td><td>95</td></tr>
<tr><td>2</td><td>Tuesday</td><td>212</td></tr>
<tr><td>3</td><td>Thursday</td><td>294</td></tr>
<tr><td>4</td><td>Saturday</td><td>140</td></tr>
<tr><td>5</td><td>Friday</td><td>219</td></tr>
<tr><td>6</td><td>Wednesday</td><td>231</td></tr>
  </tbody>
	</table>
</div>
![](http://i.imgur.com/Om0miqx.png)

## Analysis_5: How is the distribution of job postings among these ten cities? what's the frequency of job posting for each city?  ##
Performed analysis on which city has the most data scientist job postings and the highest frequency of posting data scientist jobs.

![](http://i.imgur.com/o7M3kjg.png)
![](http://i.imgur.com/uCItj6M.png)
