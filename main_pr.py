import pandas as pd 
file_name='merge.xlsx'
select_core = ['X','Y']
select_status = ['A','B','C']


b_df=pd.read_excel(file_name)

filtered_noncore = b_df[b_df['column_a'].isin(select_core)]

filtered_st = filtered_noncore[filtered_noncore['STATUS'].isin(select_status)]

filtered_year = filtered_st[~filtered_st['year'].isin([2022])]
print(filtered_year[['column_a','STATUS','year']])
print('count:',filtered_year['Column_a'].count())

print('sum:',filtered_year['AMOUNT'].sum())