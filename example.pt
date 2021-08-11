from module import *
webdriver_service = service.Service(r'C:\Users\USER\AppData\Local\Programs\Opera\77.0.4054.254\operadriver.exe')
webdriver_service.start()
capabilities = {
   'operaOptions': {
        'binary': r'C:\Users\USER\AppData\Local\Programs\Opera\77.0.4054.203\opera.exe'
    }
}
driver = webdriver.Remote(webdriver_service.service_url, webdriver.DesiredCapabilities.OPERA)
set_driver(driver)
urls=search('cat')
download_urls(urls,os.getcwd())
