from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get("https://play2048.co/")

htmlElement = browser.find_element_by_tag_name("html")
while True:
    htmlElement.send_keys(Keys.UP)
    htmlElement.send_keys(Keys.RIGHT)
    htmlElement.send_keys(Keys.DOWN)
    htmlElement.send_keys(Keys.LEFT)
