##  05/06/2020
##  Author: Pierce Phillips
##  Data Cleaning
##  Salary Prediction Project


## scraping data 
import webScraper as ws
import pandas as pd
path = 'C:/Users/pphil/Salary Regression/chromedriver'
df = ws.get_jobs('software developer', 209, False, path)
df2 = ws.get_jobs('data scientist', 209, False, path)
df3 = ws.get_jobs('computer scientist', 209, False, path)
df4 = ws.get_jobs('software engineer', 209, False, path)
df5 = ws.get_jobs('mobile developer', 209, False, path)

frames = [df, df2, df3, df4, df5]
## concatinating results
result = pd.concat(frames)

## dropping duplicates
result.drop_duplicates(inplace=True)
print(result)

## convert to .csv
result.to_csv('glassdoor_jobs.csv', index = False)