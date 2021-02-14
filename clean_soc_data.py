import pandas as pd
import os

# Set crosswalk
crosswalk = pd.read_excel("https://www.bls.gov/emp/classifications-crosswalks/nem-occcode-acs-crosswalk.xlsx", dtype='str', skipline=4)
crosswalk = crosswalk.rename(columns={'Hybrid SOC Code': 'soc_code',
                                      'National Employment Matrix/SOC Occupational Title': 'soc_title',
                                      'ACS Code': 'acs_code',
                                      'ACS Occupational Title': 'acs_title'})

crosswalk.set_index('Sort Order', inplace=True)

# Process Degree of Automation
automation = pd.read_csv('Degree_of_Automation.csv', dtype='str')

# Import other files
skills = pd.read_xslx('Skills.xlsx', dtype='str')
career_change = pd.read_excel('Career Changers Matrix.xlsx', dtype='str')
tech_skill = pd.read_excel('Technology Skills.xlsx', dtype='str')
sample_titles = pd.read_excel('Sample of Reported Titles.xlsx', dtype='str')
exposure = pd.read_excel('Exposure To Infection Disease.xlsx', dtype='str')
emerging_tasks = pd.read_excel('Emerging Tasks.xlsx', dtype='str')
skills_to_work = pd.read_excel('Skills to Work Activities.xlsx', dtype='str')
onet_structure = pd.read_excel('ONET SOC_Structure.csv', dtype='str')
