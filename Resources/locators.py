from selenium.webdriver.common.by import By


class HomePageLocators():

    textbox_username = (By.ID,"login_field")
    textbox_password = (By.ID,"password")

    button_login = (By.CLASS_NAME,"js-sign-in-button")


