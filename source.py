#!/usr/bin/env python
# coding: utf-8

# # {Project Title}📝
# 
# ![Banner](./assets/banner.jpeg)

# ## Topic
# *What problem are you (or your stakeholder) trying to address?*
# 📝 <!-- Answer Below -->
# ##
# The impacts of phone screen time on student well being and academic performace. 

# ## Project Question
# *What specific question are you seeking to answer with this project?*
# *This is not the same as the questions you ask to limit the scope of the project.*
# 📝 <!-- Answer Below -->
# ## 
# How do different patterns of screen time including academic use vs. non academic use bedtime screen time habits, and the use of screen time managemnt tools affect student GPA, sleep quality, and well being?

# ## What would an answer look like?
# *What is your hypothesized answer to your question?*
# 📝 <!-- Answer Below -->
# ##
# I hypothesize that toal screen time per day is negatively correlated with student GPA especially when screen time is used more for non academic use. Then I think academic screen time may show a positive or somewhat neutral correlation while bedtime screen time likely messes with sleep duration and qaulity which would contribute to poor academic and mental health outcome. Lastly I think that students who use screen time management tools will show better sleep, higher GPA, and a better well being. 

# ## Data Sources
# *What 3 data sources have you identified for this project?*
# *How are you going to relate these datasets?*
# 📝 <!-- Answer Below -->
# ##
# 1. Screen Time Data (Github/CSV)
# https://github.com/rashakil-ds/Public-Datasets/blob/main/Screen%20Time%20Data.csv
# 
# 2. Teen Screen Time and Mental Health Summary(CDC/Scaped Page) 
# https://www.cdc.gov/nchs/products/databriefs/db513.htm
# 
# 3. Academic Performance Database (Kaggle/SQLite)
# https://www.kaggle.com/datasets/spscientist/students-performance-in-exams
# 
# I will compare screen time data with GPA, sleep, and mental health outcomes by matching similar categories across datasets. For example I will look at total screen time and academic screen time from the CSV file, then compare those values to GPA scores from the database. I will also use bedtime screen use and sleep data to check for patterns in sleep quality. For mental health, I willl use scraped CDC stats to see how screen time levels relate to anxiety or depression trends. Each dataset will be aligned by category or behavior to find clear relationships.
# 
# 

# ## Approach and Analysis
# *What is your approach to answering your project question?*
# *How will you use the identified data to answer your project question?* 📝
# ##
# To start I will import and clean each dataset so I can compare screen time, GPA, sleep, and mental health. Then I will group the data by categories like total screen time, academic vs. non academic use, and whether students use screen time tools. I’ll use simple visualizations to show patterns and relationships.
# 
# What my answers could look like:
# 
# - A scatter plot showing GPA compared to total screen time, with a trend line to show correlation.
# - A bar chart comparing sleep hours and sleep quality across screen time ranges (<1-2 Hours, 2-3 hours, 3+ hours, etc)
# - A stacked bar chart showing academic vs. non-academic screen time and their average GPA
# - A box plot comparing GPA and sleep duration between students who use screen time management tools and those who don’t
# 
# 
# 
# 

# ## Resources and References
# *What resources and references have you used for this project?*
# 📝 <!-- Answer Below -->
# ##
# https://pandas.pydata.org/docs/
# https://docs.python.org/3/library/sqlite3.html
# https://requests.readthedocs.io/en/latest/
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# https://github.com/Kaggle/kaggle-api
# https://seaborn.pydata.org/
# 

# In[2]:


# ⚠️ Make sure you run this cell at the end of your notebook before every submission!
get_ipython().system('jupyter nbconvert --to python source.ipynb')

