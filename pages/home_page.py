import sys
import os
sys.path.append(sys.path[0] + "/..")
from base_page import BasePage
from Resources.locators import HomePageLocators
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options




class HomePage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://github.com/login")
        
    
    def login(self, username, password):
        self.enter_text(HomePageLocators.textbox_username, username)
        self.enter_text(HomePageLocators.textbox_password, password)
        self.click(HomePageLocators.button_login)

        
if __name__ == "__main__":

    load_dotenv()
    username = os.getenv("NAME")
    password = os.getenv("PASSWORD")

    chr_options = Options()
    chr_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome( options=chr_options)
    #driver = webdriver.Chrome()
    driver.maximize_window()

    check = HomePage(driver)
    check.login(username,password)

# check = HomePage()
# HomePage.login()