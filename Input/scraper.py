# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import os

def scraper(path,url, pages):
    df = pd.DataFrame(columns=['date','school','decision','info'])
    results = []
    for i in range(1,pages):
        try:
            page = requests.get(url + str(i))
            soup = BeautifulSoup(page.content, 'html.parser')
            data = soup.find_all("div", class_="col")
            for result in data:
                info = result.find("div",class_="mt-3").text
                date = result.find("p",class_="mb-0 fst-italic").text
                school = result.find("h6", class_="mt-3 fw-normal").text
                decision = result.find("span","badge").text
                results.append([date, school, decision,info])
        except:
            pass
    df = pd.concat([df, pd.DataFrame(results,columns=df.columns)])
    df['date'] = df['date'].str.replace('Added on ','')
    df['date'] = df['date'].str.replace(',','')
    df['date'] =  pd.to_datetime(df['date'], infer_datetime_format=True)  
    df['gre_q'] = df['info'].str.extract(r'(GRE \d{3}?)',flags=re.IGNORECASE | re.MULTILINE).replace('GRE ', '', regex=True)
    df['gre_v'] = df['info'].str.extract(r'(GRE V \d{3}?)',flags=re.IGNORECASE | re.MULTILINE).replace('GRE V ', '', regex=True)
    df['gre_aw'] = df['info'].str.extract(r'(AW \d{1}.\d{2})',flags=re.IGNORECASE | re.MULTILINE).replace('AW ', '', regex=True)
    df['gpa'] = df['info'].str.extract(r'(gpa \d{1}.\d{2})',flags=re.IGNORECASE | re.MULTILINE).replace('GPA ', '', regex=True)
    df['school'] = df['school'].str.replace('Economics, ','')
    df['decision'] = df['decision'].where(~df['decision'].str.contains('Accepted'), 'Accepted', axis=0)
    df['decision'] = df['decision'].where(~df['decision'].str.contains('Rejected'), 'Rejected', axis=0)
    df['decision'] = df['decision'].where(~df['decision'].str.contains('Wait'), 'Wait Listed', axis=0)
    df['decision'] = df['decision'].where(~df['decision'].str.contains('Interview'), 'Interview', axis=0)
    df.to_csv(path_or_buf=os.path.abspath(os.path.join(path,'df.csv')),index=False)

   