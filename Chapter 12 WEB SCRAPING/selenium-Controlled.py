# from selenium import webdriver
# browser = webdriver.Firefox()
#
#
# browser.get('https://inventwithpython.com')
# try:
#     elem = browser.find_element_by_class_name('cover-thumb')
#     print('Found <%s> element with that class name!' % (elem.tag_name))
# except:
#     print('Was not able to find an element with that name.')
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
browser.get("https://nostarch.com")
htmlElem = browser.find_element_by_tag_name("html")
htmlElem.send_keys(Keys.END)
htmlElem.send_keys(Keys.HOME)
browser.quit()