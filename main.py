import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = ['https://www.youtu.be/QxhUZaQyeLY', 'https://www.youtu.be/1gIiq7uC-C4', 'https://www.youtu.be/Qa1yYCc30yo',
       'https://www.youtu.be/dtMSpmMZNTw', 'https://www.youtu.be/Dlm3uMXjaT8', 'https://www.youtu.be/Uf_BA6Tzrik',
       'https://www.youtu.be/d0XwIn3gASM', 'https://www.youtu.be/McF4QIh0qMM', 'https://www.youtu.be/uj6y5N5ZO_I']

url_inverso = []

for i in range(0, len(url)):
    link = url[len(url) - i - 1]
    url_inverso.append(link)

pagine_da_aprire = 1

for link in url_inverso:
    indirizzo = 'https://it1.savefrom.net/106/#url=' + link + '?noredirect=1&'
    browser = webdriver.Chrome()
    browser.get(indirizzo)
    time.sleep(10)

    bassa_qualita_botton = browser.find_element(By.XPATH, '//a[@class="uvd-promo__mq_btn-new ga_track_events"]')
    bassa_qualita_botton.click()
    time.sleep(5)

    download = browser.find_element(By.XPATH, '//a[@class="link link-download subname ga_track_events download-icon"]')
    download.click()
    time.sleep(3)

    if len(browser.window_handles) > pagine_da_aprire:
        scheda_pubblicita = browser.window_handles[1]
        browser.switch_to.window(scheda_pubblicita)
        browser.close()

    time.sleep(10)

    while any(filename.endswith(".crdownload") for filename in os.listdir(r"C:\Users\User\Downloads")):
        time.sleep(10)

    browser.quit()
