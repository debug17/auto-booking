from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

service = EdgeService(executable_path="D:\\a\p\msedgedriver.exe")
options = webdriver.EdgeOptions()
driver = webdriver.Edge(service=service, options=options)


driver.get("https://cgyy.zzuli.edu.cn")
sleep(1)

dl=driver.find_element(By.CLASS_NAME,"button-transition").click()
sleep(3)

active=driver.find_element(By.CLASS_NAME,"active").click()
sleep(3)

mm = driver.find_element(by=By.XPATH,value="/html/body/spring:theme/div[2]/div/div[2]/form/div[1]/div[2]/h3").click()
sleep(5)

driver.quit()