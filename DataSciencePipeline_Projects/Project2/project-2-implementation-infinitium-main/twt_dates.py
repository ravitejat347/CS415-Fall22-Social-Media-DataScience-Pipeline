#after pip install pandas, import the module
import pandas as pd 

#Read your input csv file
df = pd.read_csv('twt_ab.csv')

#Convert all the string values of date-time column to datetime objects
df['date-time-obj'] = pd.to_datetime(df['time'])

#Create two new columns with date-only and time-only values
df['_id.year'] = df['date-time-obj'].dt.year
df['_id.month'] = df['date-time-obj'].dt.month
df['_id.day'] = df['date-time-obj'].dt.day
df['_id.hour'] = df['date-time-obj'].dt.hour
#Deleted temporarily created column
del df['date-time-obj']

#Save your final data to a new csv file
df.to_csv('tw_abt.csv', index=False)