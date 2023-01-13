import pytest

from pages.home_page import HomePage
from selenium import webdriver

class Test_page_login():


    def test_login(self):
        self.driver = webdriver.Chrome()
        self.