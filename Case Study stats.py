# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 11:44:56 2021

@author: DELL001
"""
import pandas as pd
from scipy import stats


main_data = pd.read_excel(r"Case Studty - Retention.xlsx", sheet_name = 'Case Studty - Retention')
main_data['Client Name'].value_counts() 


#Hypothesis 1 - considering all policies
hyp1_data = main_data.groupby(['Client Level 1 (Segment)','Client Name'])['Retention_Hyp1_All'].sum()
hyp1_data = pd.DataFrame(hyp1_data).reset_index(drop= False)

key_client_ret = hyp1_data[hyp1_data['Client Level 1 (Segment)'] == 'Key Clients']['Retention_Hyp1_All']
non_key_client_ret = hyp1_data[hyp1_data['Client Level 1 (Segment)'] != 'Key Clients']['Retention_Hyp1_All']

stats.ttest_ind(key_client_ret ,non_key_client_ret)  



#Hypothesis 2 - considering all policies
hyp2_data = main_data.groupby(['Principle MLOB','Client Name'])['Retention_Hyp2_All'].sum()
hyp2_data = pd.DataFrame(hyp2_data).reset_index(drop= False)

Prop_client_ret = hyp2_data[hyp2_data['Principle MLOB'] == 'Property']['Retention_Hyp2_All']
Liab_client_ret = hyp2_data[hyp2_data['Principle MLOB'] == 'Liability']['Retention_Hyp2_All']

stats.ttest_ind(Prop_client_ret ,Liab_client_ret)  


#Hypothesis 3 - considering all policies
hyp3_data = main_data.groupby(['Retention_with_1M','Client Name'])['Retention_Hyp1_All'].sum()
hyp3_data = pd.DataFrame(hyp3_data).reset_index(drop= False)

High_prem_client_ret = hyp3_data[hyp3_data['Retention_with_1M'] == 'Y']['Retention_Hyp1_All']
Low_prem_client_ret = hyp3_data[hyp3_data['Retention_with_1M'] == 'N']['Retention_Hyp1_All']

stats.ttest_ind(High_prem_client_ret ,Low_prem_client_ret)  



main_data.groupby('Client Level 1 (Segment)')['Retention_Hyp1'].mean()

main_data['UW Year'][-1:]

main_data.columns