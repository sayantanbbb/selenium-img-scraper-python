
# Selenium python img scraper

This is an module which may help you to scrape images from google using selenium , it can be used for ml datasets or data scraping



## Example

```
from module import *
# Load your driver through required code
#webdriver_service = service.Service(r'C:\Users\USER\AppData\Local\Programs\Opera\77.0.4054.254\operadriver.exe')
#webdriver_service.start()
#capabilities = {
#   'operaOptions': {
#        'binary': r'C:\Users\USER\AppData\Local\Programs\Opera\77.0.4054.203\opera.exe'
#   }
#}

#driver = webdriver.Remote(webdriver_service.service_url, webdriver.DesiredCapabilities.OPERA)
set_driver(driver) # Set the driver
urls=search('cat') # Search the query in google and get the urls
download_urls(urls,os.getcwd()) # download the urls in the directory you want (os.getcwd())
```

## download

You need wget installed for these commands to run otherwise you can download them manually
```
$ wget https://raw.githubusercontent.com/sayantanbbb/selenium-img-scraper-python/master/module.py
$ wget https://raw.githubusercontent.com/sayantanbbb/selenium-img-scraper-python/master/requirements.txt
$ pip install -r requirements.txt
$ python <your code file>
```
## Setup

The following commands given above will only work if you have you code file in the same directory as module.py file
Otherwise you can add module.py to enviorment variables and you should have no problems






  
