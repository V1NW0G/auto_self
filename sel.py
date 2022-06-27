from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install())

driver.get("http://172.22.196.232/sg/system/")
driver.find_element(By.ID, "edit-name").send_keys("123")
driver.find_element(By.ID, "edit-pass").send_keys("123")
driver.find_element(By.ID, "edit-submit").click()
input()
