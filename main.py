from time import sleep
from time import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome('./chromedriver')
driver.get('http://typingx0.net/sushida/play.html')
webgl_element = driver.find_element_by_xpath('//*[@id="game"]/div')
actions = ActionChains(driver)
actions.move_to_element(webgl_element).perform()

sleep(200)

actions.move_to_element_with_offset(webgl_element, 250, 255).click().perform()
actions.move_to_element_with_offset(webgl_element, 250, 300).click().perform()

element = driver.find_element_by_xpath('/html/body')
element.send_keys(" ")
start = time()
while time()-start<125.0:
  element.send_keys("abcdefghijklmnopqrstuvwxyz-!?.,")

input("入力して終了")
driver.close()
driver.quit()
