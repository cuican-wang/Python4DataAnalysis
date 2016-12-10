# INFO7374 18218 Data Analysis Using Python - Fall 2016 #
## Final Project - Exploration of Data Scientist ##
This project is mainly about Data Scientist:

1. Data is web scraped from Monster.com and Indeed.com among ten mainly IT cities(San-Francisco, Boston, Palo Alto, Chicago, New-York, Washington, Seattle, Atlanta, Houston, San-Diego)
2. How are skill-sets and degree needed among different city and different size of companies?
3. What about everyone's comments on the company?
4. Which day of a week does HR usually post jobs?
5. How is the distribution of job posting among these ten cities? what's the frequency of job posting for each city? 

## Collect Data ##
Data is web scraped and integrated from both Monster.com and Indeed.com among ten cities(San-Francisco, Boston, Palo Alto, Chicago, New-York, Washington, Seattle, Atlanta, Houston, San-Diego) including 5392 rows and 65 columns.

## Data Pre-exploration ##
Break down the whole data according to city and job post date. After pre-exploration, data is as following:
![Data root](http://i.imgur.com/VSU48Od.png)
![City root directory](http://i.imgur.com/gmPufKR.png)
![Test data](http://i.imgur.com/ChP1TAW.png)

## Analysis_1 ##
Performed sentiment analysis of companies' reviews and got a review score by using indicoio api. Higher score means more positive and lower score mean more negative. This analysis is dynamic, you can input city name and number of companies with Top and Last score. Part of the results are as following:

![Overall](http://i.imgur.com/jOvtZLk.png)
![Palo-Alto](http://i.imgur.com/3WKJxmw.png)
![Seattle](http://i.imgur.com/UWDlw3r.png)
![Boston](http://i.imgur.com/JBrlwkn.png)

## Analysis_2 ##
Performed analysis on skill-sets and degree mentioned in different job description among ten cities. You can input the city name you are interested in. Part of the results are as following:

**Over all cities:**
![](http://i.imgur.com/hUQylgJ.png)
![](http://i.imgur.com/8j6tDmb.png)
![](http://i.imgur.com/sjMfW7C.png)
![](http://i.imgur.com/9q0QqdP.png)
![](http://i.imgur.com/Z64Dc7f.png)

## Analysis_3 ##
Performed analysis on skill-sets and degree mentioned in different job description among large,medium and small companies (divided by number of employees). You can input the kind of company you are interested in. Part of the results are as following:

**Large companies**
![](http://i.imgur.com/nkXeF8A.png)
![](http://i.imgur.com/lmd6B8G.png)
![](http://i.imgur.com/b1HWZIw.png)
![](http://i.imgur.com/8Shg1so.png)
![](http://i.imgur.com/ezzEVPE.png)

## Analysis_4 ##
Performed analysis on which day of a week usually have the most job postings. You can input the time period but I recommend the period as from 2016-10-17 to 2016-11-13 due to there are no holidays and timeliness factor. Part of the results are as following:

![](http://i.imgur.com/Om0miqx.png)

## Analysis_5 ##
Performed analysis on which city has the most data scientist job postings and the highest frequency of posting data scientist jobs. Results are as following:

![](http://i.imgur.com/o7M3kjg.png)
![](http://i.imgur.com/uCItj6M.png)