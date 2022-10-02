import pandas as pd 
import re


print('start_laew_ja')
excel_file_name='excel_file.xlsx'
excel_output_file_name='excel_file_result.xlsx'#ตั้งชื่อไฟล์ผลลัพธ์

df=pd.read_excel(excel_file_name) 
print('read_file')
filtered_column_a=df[df['column_a']=='AAA']

filtered_contain_alpb=filtered_column_a[filtered_column_a['REMARK'].str.contains('[A-Za-z]',na=False)]

def cut_at_1st_alphabet(remark):
    res=re.search(r'[A-Za-z]',remark)
    if(res is None):
        return '-'
    #return f'{res.start()}#{ remark[res.start():]}' 
    return remark[res.start():]

filtered_contain_alpb['remark_cut'] = filtered_contain_alpb['REMARK'].apply(cut_at_1st_alphabet).str.replace(r'[^A-Za-z0-9\s-]','_').str.replace('x000D_',"")



contain_number=filtered_contain_alpb[filtered_contain_alpb['remark_cut'].str.contains('[A-Za-z]')]

contain_number=contain_number[contain_number['remark_cut'].str.contains('[0-9]')]
 

contain_number.to_excel(excel_output_file_name,index=False)

print('done')