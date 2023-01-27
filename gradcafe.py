# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 17:00:53 2023

@author: juani
"""

import os

path = os.path.join(os.environ['USERPROFILE'])+r'\OneDrive\Documentos\Google Drive\Coding\Python\BOTs\PhD'
os.chdir(path)

from scraper import scraper
from cleaner import cleaner, checker

url = "https://www.thegradcafe.com/survey/?institution=&program=Economics&degree=PhD&page="
pages = 4
scraper(path,url,pages)
cleaner(path,'econnn')



