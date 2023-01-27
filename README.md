## Using gradcafe.py

To use gradcafe.py, follow these steps:

* Complete with your data:

```python
import os
path = os.path.join(os.environ['USERPROFILE'])+r'\Desktop\Python\GitHub'  #set your path
from scraper import scraper
from cleaner import cleaner, checker  

url = "https://www.thegradcafe.com/survey/?institution=&program=Economics&degree=PhD&page=" #set the gradcafe url to scrape (i.e. program and degree)
pages = 4 #integer value of pages you want to scrape
scraper(path,url,pages)
cleaner(path,'econnn') #The second variable is a string one, useful to identify the data of the program you are scraping.
```

* Compile and run the code, it will collect all the data from the number of pages you have entered, and export it as nice formatted matrix as an Excel file.

## Contact
If you want to contact me, you can reach me at juanidinaro@gmail.com
