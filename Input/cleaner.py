# -*- coding: utf-8 -*-
import pandas as pd
import os
from fuzzywuzzy import fuzz 
from fuzzywuzzy import process

def checker(wrong_options,correct_options):
    names_array=[]
    ratio_array=[]    
    for wrong_option in wrong_options:
        if wrong_option in correct_options:
           names_array.append(wrong_option)
           ratio_array.append('100')
        else:   
            x=process.extractOne(wrong_option,correct_options,scorer=fuzz.token_set_ratio)
            names_array.append(x[0])
            ratio_array.append(x[1])
    return names_array,ratio_array

def cleaner(path,program):
    df = pd.read_csv(os.path.abspath(os.path.join(path,'df.csv')),sep=",",header=0)
    dic = pd.read_excel(os.path.abspath(os.path.join(path,'dict_univ.xlsx')))
    match = dic['university'].tolist()
    orig = df['school'].tolist()    
    name_match,ratio_match=checker(orig,match)
    df['university']=pd.Series(name_match)
    df.to_excel('df_'+program+'.xlsx',index=False)

    