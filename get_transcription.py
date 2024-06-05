import mysql.connector
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

def _setup_driver():
    print('Loading...')
    chrome_options = Options()
    chrome_options.add_argument("disable-infobars")
    chrome_options.binary_location = r'/usr/local/bin/chromium'
    driver = webdriver.Chrome(options=chrome_options)
    #driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    return driver

mysql_db = mysql.connector.Connect(
             host = "findwordvideo.mysql.dbaas.com.br",
             user = "findwordvideo",
             password = "Locaweb@2",
             database = "findwordvideo"
           )
        
cursor = mysql_db.cursor()
cursor.execute('select * from video_inf')    
videos = cursor.fetchall()

driver = _setup_driver()

for video in videos:
    driver.get(f'https://ytscribe.com/v/{video[3]}')
    break
