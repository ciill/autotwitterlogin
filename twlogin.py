from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

print("Welcome to Omar Hegazy's Auto Twitter Login Bot.")
print("")
time.sleep(2)
class TwitterBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.twitter.com/")
        time.sleep(5)
        user_name_elem = driver.find_element_by_name("session[username_or_email]")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        password_elem = driver.find_element_by_name("session[password]")
        password_elem.clear()
        password_elem.send_keys(self.password)
        password_elem.send_keys(Keys.RETURN)
        time.sleep(2)

omarTW = TwitterBot(input("Enter Username: "),input("Enter Password: "))
omarTW.login()