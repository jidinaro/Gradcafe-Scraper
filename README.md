## Using gradcafe.py

To use gradcafe.py, follow these steps:

* Complete with your data:

```python
import os
path = os.path.join(os.environ['USERPROFILE'])+r'\Desktop\Python\GitHub'  #set your path
from scraper import scraper
from cleaner import cleaner, checker  

url = "https://www.thegradcafe.com/survey/?institution=&program=Economics&degree=PhD&page=" #set the gradcafe url to scrape (i.e. program and degree)
pages = 4
rnkg(URL,path,rank) #Call this function as many times as you need (i.e.: subjects)
```

* Compile and run the code, it will collect all the ranking urls and export them as Excel files.

## Contact
If you want to contact me, you can reach me at juanidinaro@gmail.com
