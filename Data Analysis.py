#!/usr/bin/env python
# coding: utf-8

# In[29]:


import pandas as pd


'''
Task 1: The percentage of renters in an area who are spending 30% or more of their income on 
shelter costs is represented as shelt_rent_30plus_rate in the “BC census 2016 data.csv” file. 
Find out the Community Health Service Areas (chsa) whose shelt_rent_30plus_rate are more than 
50%. Considering these areas’ household income and rent prices, are the rental subsidization 
rates of these areas appropriate?

Task 2: Now let’s focus on examining the data at the “regional” level ofProvincial Health
Authority (pha): Fraser, Interior, Northern, Vancouver Coastal, and Vancouver Island. 
Determine whether or not shelter subsidization rates differ across the five pha regions.

Project by: Luca Steiner
'''


## Finding the Community Health Service Areas (chsa) whose shelt_rent_30plus_rate are more than
## 50%.
df=pd.read_csv('BC Census 2016 data.csv')
plus_50 = df.loc[(df['shelt_rent_30plus_rate'] > 50) ]
chsa = plus_50['chsa']
print(f'The Community Health Service areas where 50% of the population spend 30% of their income on rent are: \n\n{chsa}')


shelt_sub_50 = round(plus_50['shelt_rent_subsidized_rate'].mean(),2)
income_after_tax50 = round(plus_50['income_after_tax_median'].mean(), 2)
print(f'\n The mean rental subsidization rate of areas where 50% of the population spend 30% or more of their income on rent is: {shelt_sub_50}')
print(f'\n The mean of the median income after tax of areas where 50% of the population spend 30% or more of their income on rent is: {income_after_tax50} \n\n\n')


## Less than 50%
shelt_rate_other = df.loc[(df['shelt_rent_30plus_rate'] < 50) ]
chsa_other = shelt_rate_other['chsa']
print(f'\nThe Community Health Service areas where less than 50% of the population spend 30% of their income on rent are: \n\n{chsa_other}')

shelt_sub_other = round(shelt_rate_other['shelt_rent_subsidized_rate'].mean(),2)
income_after_tax_other = round(shelt_rate_other['income_after_tax_median'].mean(),2)
print(f'\nThe mean rental subsidization rate of areas where less than 50% of the population spend 30% or more of their income on rent is: {shelt_sub_other}')
print(f'\nThe mean of the median income after tax of areas where 50% of the population spend 30% or more of their income on rent is: {income_after_tax_other} \n\n\n')


## statement about data
print('Given the mean of the median income in each Community Health Service Area, when comparing the shelter \nsubsidy rate, the CHSAs with 50% or more of their population spending 30% or more of their income on \nrent should be subsidized more than they currently are. They are appropriate, but could be better.\n')
print(f'{shelt_sub_50} > {shelt_sub_other}, but {income_after_tax50} < {income_after_tax_other} therefore it seems like the subsidy rate in the expensive areas could be higher') 



## Determining if shelter subsidization rate differs across different PHA's
fraser = df.loc[df['pha'] == 'Fraser' ]
interior = df.loc[df['pha'] == 'Interior' ]
northern = df.loc[df['pha']== 'Northern' ]
vancouver = df.loc[df['pha'] == 'Vancouver Coastal' ]
island = df.loc[df['pha']=='Vancouver Island']

## subsidization rates
fraser_shelt = fraser['shelt_rent_subsidized_rate'].mean()
interior_shelt = interior['shelt_rent_subsidized_rate'].mean()
northern_shelt = northern['shelt_rent_subsidized_rate'].mean()
vancouver_shelt = vancouver['shelt_rent_subsidized_rate'].mean()
island_shelt = island['shelt_rent_subsidized_rate'].mean()

## showing results
print('Below is how the subsizadation rates differ across PHAs: \n\n')
print(f'The subsidization rate of Fraser PHA: {fraser_shelt}\n')
print(f'The subsidization rate of Interior PHA: {interior_shelt}\n')
print(f'The subsidization rate of Northern PHA: {northern_shelt}\n')
print(f'The subsidization rate of Vancouver PHA: {vancouver_shelt}\n')
print(f'The subsidization rate of Island PHA: {island_shelt}\n')

## statement about results
print(f'As shown above, the Vancouver PHA has a subsidization rate of {vancouver_shelt}, substancially  \nhigher than the other 4. This makes sense given Vancouvers housing market.')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




