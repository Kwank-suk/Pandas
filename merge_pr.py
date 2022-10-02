import pandas as pd 

f1 = pd.read_excel('f1.xlsx',sheet_name='data')
f2= pd.read_excel('f2.xlsx',sheet_name='data')
f3=pd.read_excel('f3.xlsx',sheet_name='data')

merge = pd.concat([f1,f2,f3],ignore_index=True)

merge.to_excel('merge.xlsx',index=False)