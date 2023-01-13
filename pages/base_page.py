from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BasePage():

    def __init__(self, driver):
        self.driver = driver


    def click(self, locator):
        """ Performs click on web element whose locator is passed to it"""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    def enter_text(self, locator, text):
        """ Performs text entry of the passed in text, in a web element whose locator is passed to it"""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)


    def get_element_text(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element.text


    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title
    