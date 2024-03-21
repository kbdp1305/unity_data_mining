from appium import webdriver
from appium.options.android import UiAutomator2Options
desired_cap={
  "appium:platformName": "Android"
}

APPIUM_PORT = 4723
APPIUM_HOST = 'localhost'
options = UiAutomator2Options()
driver=webdriver.Remote(f'http://{APPIUM_HOST}:{APPIUM_PORT}/wd/hub',options=options)
driver.implicitly_wait(10)

driver.find_element('00000000-0000-127f-ffff-ffff000014f7').click()