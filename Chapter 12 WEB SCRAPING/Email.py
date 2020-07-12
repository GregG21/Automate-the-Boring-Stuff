
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def Email(email, string):
    browser = webdriver.Firefox()
    browser.get("https://mail.google.com/mail/u/0/")

    emailAddressField = browser.find_element(By.TAG_NAME, "input")
    emailAddressField.send_keys("atbstest4@gmail.com")
    emailAddressField.send_keys(Keys.ENTER)

    wait = WebDriverWait(browser, 10) #most time it waits if not clickable
    passwwordInput = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='password']")))
    passwwordInput.send_keys("Gabric123")
    passwwordInput.send_keys(Keys.ENTER)


    compose = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "aic")))
    compose.click()

    fillOutEmail = wait.until(EC.element_to_be_clickable((By.XPATH, "//textarea")))
    fillOutEmail.send_keys(email)

    fillOutSubject = browser.find_element(By.CSS_SELECTOR, "input[name='subjectbox']")
    fillOutSubject.send_keys("THIS IS AN AUTOMATED MESSAGE")


    fillOutMessage = browser.find_element(By.CSS_SELECTOR, "div[aria-label='Message Body']")
    fillOutMessage.send_keys(string)
    fillOutMessage.send_keys(Keys.CONTROL + Keys.ENTER)

    browser.close()






Email("rakomarusa@gmail.com","ZANDJE SPOROCILO ")





