from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

service = EdgeService(executable_path="D:\\a\p\msedgedriver.exe")
options = webdriver.EdgeOptions()
driver = webdriver.Edge(service=service, options=options)


driver.get("https://cn.bing.com/?mkt=zh-CN")

sleep(5)
print(driver.title)
news=driver.find_element(By.CLASS_NAME,"tob_title")
print(news.text)

sou=driver.find_element(By.CLASS_NAME,"sb_form_q").click()
#sou.send_keys("text")
ActionChains(driver).send_keys_to_element(sou, "text").perform()
sleep(2)

driver.quit()