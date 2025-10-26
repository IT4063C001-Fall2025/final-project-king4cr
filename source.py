#!/usr/bin/env python
# coding: utf-8

# # Phones vs. Students📝
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
# 2. Academic Performance Database (Kaggle)
# https://www.kaggle.com/datasets/spscientist/students-performance-in-exams
# 
# 3. Teen Phone Addiction (Github/CSV)
# https://github.com/shrisha337-beep/Smartphone-Usage-Analysis/blob/main/teen_phone_addiction_dataset.csv
# 
# 4. User Behavior (Kaggle)
# https://www.kaggle.com/datasets/valakhorasani/mobile-device-usage-and-user-behavior-dataset?resource=download
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

# ## Check Point 2

# 
# ## Exploratory Data Analysis (EDA)
# 
# What insights and interesting information are you able to extract at this stage?
# 
# - The screen time data tracks daily usage across different categories like social networking, reading, productivity, etc.
# 
# - Social networking consistently shows the highest usage among all categories
# 
# - Student performance data includes academic scores across three subjects (math, reading, writing) along with demographic and educational factors.
# 
# - The data includes information about test preparation and parental education levels
# What are the distributions of my variables?
# 
# 
# What are the distributions of my variables?
# 
# - Screen Time variables show daily fluctuations, with most activity concentrated in Social Networking
# 
# - Total Screen Time appears to vary between 50-200 minutes per day
# 
# - Student test scores appear to be normally distributed, typically ranging from 40-95
# 
# - Reading and Productivity categories show moderate usage, while Gaming and Other categories have lower engagement.
# 
# Are there any correlations between my variables?
# 
# - There's likely a strong correlation between all three test scores with math, reading, writing
# 
# - Screen time categories show some correlation with total screen time
# 
# - Social Networking appears to have the strongest correlation with Total Screen Time
# 
# 
# What issues can you see in your data at this point?
# 
# - Some screen time categories like yoga and creativity have many zero values
# 
# - The datasets are from different sources and will need integration
# 
# - The time periods for the datasets may not align perfectly
# 
# Are there any outliers or anomalies? are they relevant to your analysis? or should they be removed?
# 
# - There appear to be some extremely high screen time days 
# 
# - Some test scores show unusually low values 
# 
# - These outliers are likely relevant to my analysis and should will be kept as they represent real behavior patterns
# 
# Are there any missing values? how are you going to deal with them?
# 
# - The Screen Time data appears complete for the main categories
# 
# - Student Performance data appears to have complete entries for test scores
# 
# - I am not seeing significant missing value issues as of now
# 
# Are there any duplicate values? how are you going to deal with them?
# 
# - Some screen time patterns might repeat across days
# 
# - Student performance data likely has unique entries per student
# 
# - I will check duplicates to ensure they represent genuine repeated measurements
# 
# Are there any data types that need to be changed?
# 
# - Dates in the Screen Time data should be converted to datetime format
# - Week Day could be converted to a categorical type
# 
# - Test scores could be converted to integer type if they're not already
# 
# - Categorical variables in the Student Performance data like gender and race/ethnicity  might need to be properly encoded for analysis

# ## Data Visualization and Insights

# In[ ]:


import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

# Load  datasets
screen_time_df = pd.read_csv('dataSources/Screen_Time_Data.csv')
student_performance_df = pd.read_csv('dataSources/StudentsPerformance.csv')

# 1. Bar plot of average screen time by category
screen_categories = ['Social Networking', 'Reading and Reference', 'Productivity', 'Entertainment']
avg_screen_time = screen_time_df[screen_categories].mean().sort_values(ascending=False)

plt.figure(figsize=(10, 5))
avg_screen_time.plot(kind='bar')
plt.title('Average Daily Screen Time by Category')
plt.ylabel('Minutes')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Line plot of total screen time over time
plt.figure(figsize=(10, 5))
plt.plot(screen_time_df['Date'], screen_time_df['Total Screen Time '])
plt.title('Daily Total Screen Time')
plt.xlabel('Date')
plt.ylabel('Minutes')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. Histogram of test scores
plt.figure(figsize=(10, 5))
plt.hist(student_performance_df['math score'], bins=20, alpha=0.5, label='Math')
plt.hist(student_performance_df['reading score'], bins=20, alpha=0.5, label='Reading')
plt.hist(student_performance_df['writing score'], bins=20, alpha=0.5, label='Writing')
plt.title('Distribution of Test Scores')
plt.xlabel('Score')
plt.ylabel('Number of Students')
plt.legend()
plt.tight_layout()
plt.show()

# 4. Bar plot comparing average scores by test preparation
prep_comparison = student_performance_df.groupby('test preparation course')[['math score', 'reading score', 'writing score']].mean()
prep_comparison.plot(kind='bar', figsize=(10, 5))
plt.title('Average Test Scores by Test Preparation')
plt.ylabel('Average Score')
plt.xlabel('Test Preparation Course')
plt.legend(title='Subject')
plt.tight_layout()
plt.show()


# 
# 
# ### 1. Average Daily Screen Time by Category
# This bar chart shows the average time spent on different activities. Key insights:
# - Social Networking dominates screen time usage
# - Reading and Reference activities show moderate usage
# - Productivity tools have lower average usage
# - Entertainment shows relatively low usage compared to social activities
# 
# ### 2. Daily Total Screen Time Trend
# The line plot tracks total screen time over dates. Key insights:
# - Screen time varies significantly day to day
# - Some days show spikes in usage (possibly weekends or specific events)
# - The pattern might reveal weekly cycles in screen time usage
# - Helps identify any unusual days with very high or low usage
# 
# ### 3. Test Score Distributions
# The overlapping histograms show the distribution of scores across subjects. Key insights:
# - Most scores fall between 60-80 range
# - Reading and writing scores tend to be similarly distributed
# - Math scores show slightly different distribution patterns
# - We can see if any subject has more extreme scores (very high or very low)
# 
# ### 4. Impact of Test Preparation
# The bar chart compares test scores between students who completed test prep and those who didn't. Key insights:
# - Shows whether test preparation improves scores
# - Reveals which subjects benefit most from test preparation
# - Helps understand if test prep impact varies by subject
# - Can guide recommendations about test preparation effectiveness

# ## Data Cleaning and Transformation
# 
# Gather initial data:

# In[11]:


# Import required libraries
import pandas as pd
import numpy as np
from scipy import stats

# Reload the original datasets to start fresh
screen_time_df = pd.read_csv('dataSources/Screen_Time_Data.csv')
student_performance_df = pd.read_csv('dataSources/StudentsPerformance.csv')

# Display initial info about our datasets
print("Initial Screen Time Data Info:")
print(screen_time_df.info())
print("\nInitial Student Performance Data Info:")
print(student_performance_df.info())


# ### Data Type Transformations
# Convert  data columns to their appropriate types:
# - Dates should be datetime objects
# - Screen time values should be numeric
# - Categorical variables should be properly encoded

# In[ ]:


# Convert date to datetime
screen_time_df['Date'] = pd.to_datetime(screen_time_df['Date'])

# Convert Week Day to categorical with proper order
week_day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
screen_time_df['Week Day'] = pd.Categorical(screen_time_df['Week Day'], categories=week_day_order, ordered=True)

# Make all screen time values are numeric
numeric_columns = ['Total Screen Time ', 'Social Networking', 'Reading and Reference', 
                  'Other', 'Productivity', 'Health and Fitness', 'Entertainment', 'Creativity', 'Yoga']
screen_time_df[numeric_columns] = screen_time_df[numeric_columns].apply(pd.to_numeric, errors='coerce')

# Convert student performance categorical variables
student_performance_df['test preparation course'] = pd.Categorical(student_performance_df['test preparation course'])
student_performance_df['gender'] = pd.Categorical(student_performance_df['gender'])
student_performance_df['race/ethnicity'] = pd.Categorical(student_performance_df['race/ethnicity'])

print("Updated data types in Screen Time Data:")
print(screen_time_df.dtypes)
print("\nUpdated data types in Student Performance Data:")
print(student_performance_df.dtypes)


# ### Missing Values and Duplicates
# Check for and handle any missing or duplicate data in my datasets:

# In[ ]:


# Check for missing values
print("Missing values in Screen Time Data:")
print(screen_time_df.isnull().sum())
print("\nMissing values in Student Performance Data:")
print(student_performance_df.isnull().sum())

# Check for duplicates
print("\nDuplicate rows in Screen Time Data:", screen_time_df.duplicated().sum())
print("Duplicate rows in Student Performance Data:", student_performance_df.duplicated().sum())

# Handle missing values

# Fill screen time with 0 for missing activity values
screen_time_df[numeric_columns] = screen_time_df[numeric_columns].fillna(0)

# Remove any duplicate rows
screen_time_df = screen_time_df.drop_duplicates()
student_performance_df = student_performance_df.drop_duplicates()

print("\nRemaining missing values in Screen Time Data:")
print(screen_time_df.isnull().sum().sum())
print("Remaining missing values in Student Performance Data:")
print(student_performance_df.isnull().sum().sum())


# ### Step 3: Outliers and Anomalies
# Now we'll identify and handle outliers in our numerical data.

# In[ ]:


# Ddetect outliers using IQR method
def detect_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)][column]
    return outliers

# Check for outliers in screen time
print("Outliers in Total Screen Time:")
outliers = detect_outliers(screen_time_df, 'Total Screen Time ')
print(f"Number of outliers: {len(outliers)}")
print(f"Outlier values:\n{outliers.values}")

# Check for outliers in test scores
for column in ['math score', 'reading score', 'writing score']:
    print(f"\nOutliers in {column}:")
    outliers = detect_outliers(student_performance_df, column)
    print(f"Number of outliers: {len(outliers)}")
    print(f"Outlier values:\n{outliers.values}")

# Create flags for outliers instead of removing them
screen_time_df['is_screen_time_outlier'] = (
    screen_time_df['Total Screen Time '] > 
    screen_time_df['Total Screen Time '].mean() + 2 * screen_time_df['Total Screen Time '].std()
)


# ### Step 4: Feature Engineering
# Finally, we'll create some useful derived features for our analysis.

# In[ ]:


# Features for screen time analysis
screen_time_df['is_weekend'] = screen_time_df['Week Day'].isin(['Saturday', 'Sunday'])
screen_time_df['productive_time'] = screen_time_df['Reading and Reference'] + screen_time_df['Productivity']
screen_time_df['entertainment_time'] = screen_time_df['Entertainment'] + screen_time_df['Social Networking']
screen_time_df['productive_ratio'] = screen_time_df['productive_time'] / screen_time_df['Total Screen Time ']

# Features for student performance
student_performance_df['average_score'] = student_performance_df[['math score', 'reading score', 'writing score']].mean(axis=1)
student_performance_df['score_range'] = student_performance_df[['math score', 'reading score', 'writing score']].max(axis=1) - \
                                      student_performance_df[['math score', 'reading score', 'writing score']].min(axis=1)

# Display new features
print("New features in Screen Time Data:")
print(screen_time_df[['is_weekend', 'productive_time', 'entertainment_time', 'productive_ratio']].describe())
print("\nNew features in Student Performance Data:")
print(student_performance_df[['average_score', 'score_range']].describe())


# ### Summary of Data Cleaning Process
# 
# 1. **Data Type Transformations**
#    - Converted dates to datetime format
#    - Made 'Week Day' a proper categorical variable
#    - Ensured numeric types for all measurement columns
#    - Converted categorical variables in student performance data
# 
# 2. **Missing Values and Duplicates**
#    - Checked both datasets for missing values
#    - Filled missing activity values with 0 (assuming no activity)
#    - Removed duplicate entries to prevent bias
#    - Verified all missing values were handled appropriately
# 
# 3. **Outliers Handling**
#    - Used IQR method to identify outliers
#    - Created flags for outliers instead of removing them
#    - Kept test score outliers as they represent valid scores
#    - Documented extreme values for further analysis
# 
# 4. **Feature Engineering**
#    - Added weekend/weekday indicator
#    - Created productive time and entertainment time metrics
#    - Calculated productive time ratio
#    - Added average score and score range for student performance
#    - These new features will help in analyzing patterns and relationships
# 
# The cleaned datasets are now ready for detailed analysis. We've preserved the original data while adding useful derived features and properly handling any data quality issues.

# ## Prior Feedback and Updates
# 
# - What feedback did you receive from your peers and/or the teaching team?
#     - The feed back I recieved was my code was clear and easy to follow, my logic worked well, and my use of comments helped explain each step.
# - What changes have you made to your project based on this feedback?
#     - Did not really make any changes to the way I did this part of the porject but I continued to add comments to my code to allow it to be understood by anyone who looks over it.
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

# In[1]:


# ⚠️ Make sure you run this cell at the end of your notebook before every submission!
get_ipython().system('jupyter nbconvert --to python source.ipynb')

