import pickle

from selenium import webdriver
from selenium.webdriver.common.by import By  # search elements by
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

COOKIES_PATH = 'cookies.pkl'
STARTUP_PAGE = 'https://bluearchive.jp/'


def no_image(options: webdriver.ChromeOptions):
    prefs = {'profile.managed_default_content_settings.images': 2}
    options.add_experimental_option('prefs', prefs)


options = webdriver.ChromeOptions()
# download from https://googlechromelabs.github.io/chrome-for-testing/#stable
options.binary_location = 'chrome-win64/chrome.exe'
# Bypass OS security model
options.add_argument('--no-sandbox')
# overcome limited resource problems
options.add_argument('--disable-dev-shm-usage')
# no_image(options)

driver = webdriver.Chrome(options=options)
driver.get(STARTUP_PAGE)
try:
    with open(COOKIES_PATH, 'rb') as f:
        cookies = pickle.load(f)
        print(cookies)
        for cookie in cookies:
            driver.add_cookie(cookie)
except FileNotFoundError:
    pass
driver.refresh()

# code here...
input('Press [Enter] to continue...')

with open(COOKIES_PATH, 'wb') as f:
    pickle.dump(driver.get_cookies(), f)

driver.close()
