import os
import selenium
from selenium import webdriver
import time
from selenium.webdriver.chrome import service
from datauri import DataURI
from tqdm import tqdm
import requests
#webdriver_service = service.Service(r'C:\Users\USER\AppData\Local\Programs\Opera\77.0.4054.254\operadriver.exe')
#webdriver_service.start()
#capabilities = {
#   'operaOptions': {
#        'binary': r'C:\Users\USER\AppData\Local\Programs\Opera\77.0.4054.203\opera.exe'
#    }
#}
#driver = webdriver.Remote(webdriver_service.service_url, webdriver.DesiredCapabilities.OPERA)

def set_driver(d):
    global driver
    driver=d
def get_google_url(query,sleep=3):
    url=f'https://www.google.com/search?q={query}&safe=active&sxsrf=ALeKk03OlMBjGMxKhGeY6OWQDkYrdQ23-g:1612017747573&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj9tNyJ8sPuAhXSmeYKHTZ6AqoQ_AUoAXoECA4QAw&biw=1366&bih=657'
    global driver
    driver.get(url)
    time.sleep(sleep)
def scroll(sc=1000000,sleep=5):
    global driver
    driver.execute_script(f'window.scrollBy(0, {sc})')
    time.sleep(sleep)
def press_more_images(sleep=5):
    global driver
    try:
        button=driver.find_element_by_xpath("//input[contains(@value,'Show more results')]")
        print('found Show more results')
        button.click()
        time.sleep(sleep)
        
    except:
        return False
def scan_urls():
    global driver
    imgs=driver.find_elements_by_xpath('//img')
    imgs_links=[img.get_attribute('src') for img in imgs]
    return imgs_links
def get_pexels_url(query,sleep=3):
    url=f'https://www.pexels.com/search/{query}/'
    global driver
    driver.get(url)
    time.sleep(sleep)
def download(url,file):
    if not url:
       return  
    if url.startswith('data'):
       content=DataURI(url).data
    else:
       content=requests.get(url).content
    
    open(file,'wb').write(content)
def search(query):
    get_google_url(query)
    urls=[]
    p=len(urls)
    while True:
      scroll()
      press_more_images()
      urlst=scan_urls()
      urls=list(set(urlst+urls))
      print(len(urls))
      if len(urls)==p:
         break
      p=len(urls)
    print('-----------------------')
    return urls
def download_urls(urls,dir):
    i=0
    for url in tqdm(urls):
        download(url,os.path.join(dir,'{}.jpg'.format(i)))
        i+=1

        

    
    
    
    

