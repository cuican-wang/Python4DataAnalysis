What is it

This is my midterm project. It aims to use the StackExchange REST API to collect data from stackoverflow and do some simple analysis according to the data. This project use three per-site method.
 
Main Features

Here are the main features:

function inputp():
This function is used to input parameters including topic, page, pagesize, from date, to date and so on.

function analysisOne():
This function can get data about the topic users input by calling API. Then parse the data, determine weightage by users' badges count. As a result, it can show top 3 questions according to the weightage.

function analysisTwo_1():
This function is to show all of the users' badges.

function analysisTwo_2():
This function create a file for each topic, containing user_id, user_name and link to their profile sorted by reputation.

function analysisThree():
This function shows users number for each of the badge type.

function analysisFour():
This function shows the tags attached to each of the question.

Analysis 5 is to find out the user whose questions have been upvoted the most.

Where to get it

The source code is currently hosted on GitHub at: https://github.com/cuican-wang/Python4DataAnalysis/Midterm

Dependencies

requests, json, csv, datetime, collections.



Discussion and Development

Since pandas development is related to a number of other scientific Python projects, questions are welcome on the scipy-user mailing list. Specialized discussions or design issues should take place on the PyData mailing list / Google group:

https://groups.google.com/forum/#!forum/pydata