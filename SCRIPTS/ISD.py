from selenium import webdriver
URL = input("Enter the webpage you'd like to visit\n")
category = input("What would you like to search for?\n")


browser = webdriver.Firefox()


os.makedirs("Photos", exist_ok=True)

browser.get(URL)
form = browser.find_element_by_id("search-field")
form.send_keys(category)
form.submit()

# search-for