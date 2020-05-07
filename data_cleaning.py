# -*- coding: utf-8 -*-
"""
Created on Wed May  6 15:57:16 2020

@author: pphil
"""
import pandas as pd

df = pd.read_csv('glassdoor_jobs.csv')

# salary parsing
# dropping null salary values
df = df[df['Salary Estimate']] != '-1'
# converting parsed data into measurable format
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_KD = salary.apply(lambda x: x.replace('K','').replace('$',''))
minus_Hr = minus_KD.apply(lambda x: x.lower().replace('per hour',''))
df['min_salary'] = minus_Hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = minus_Hr.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary+df.max_salary)/2

# dropping unrelated jobs, trouble spots
df = df.drop([586, 588, 590, 592, 797, 611, 549, 125, 560, 580, 584, 626, 136])
df = df.drop([374,478,610,604,444,502,597,550,625,495,531,544,559,568,679,475,554])
df = df.drop([217,235,395,114,254,236,94])
# removing rating from company name
df['Company Name'] = df.apply(lambda x: x['Company Name'] if x['Rating'] <0 else x['Company Name'][:-3], axis = 1)
# creating a state field
df['state'] = df['Location'].apply(lambda x: x.split(',')[1])
df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis = 1)
df.state.value_counts()
# creating age of company
df['age'] = df.Founded.apply(lambda x: x if x < 1 else 2020 - x)
# parsing job desc for insights
# senority

# skills
df['job_desc'] = df['Job Description']
df['python'] = df['job_desc'].apply(lambda x: 1 if 'python' in str(x).lower() else 0)
df['r_studio'] = df['job_desc'].apply(lambda x: 1 if 'r studio' in str(x).lower() else 0)
df['spark'] = df['job_desc'].apply(lambda x: 1 if 'spark' in str(x).lower() else 0)
df['tensor_flow'] = df['job_desc'].apply(lambda x: 1 if 'tensor flow' in str(x).lower() else 0)
df['sas'] = df['job_desc'].apply(lambda x: 1 if 'sas' in str(x).lower() else 0)
df['spss'] = df['job_desc'].apply(lambda x: 1 if 'spss' in str(x).lower() else 0)
df['java'] = df['job_desc'].apply(lambda x: 1 if 'java' in str(x).lower() else 0)
df['cpp'] = df['job_desc'].apply(lambda x: 1 if 'c++' in str(x).lower() else 0)
df['csharp'] = df['job_desc'].apply(lambda x: 1 if 'c#' in str(x).lower() else 0)
df['net'] = df['job_desc'].apply(lambda x: 1 if '.net' in str(x).lower() else 0)
df['devops'] = df['job_desc'].apply(lambda x: 1 if 'devops' in str(x).lower() else 0)
df['aws'] = df['job_desc'].apply(lambda x: 1 if 'aws' in str(x).lower() else 0)

df_cleaned = df
df_cleaned.to_csv('cleaned salary data.csv',index = False)
pd.read_csv('cleaned salary data.csv')