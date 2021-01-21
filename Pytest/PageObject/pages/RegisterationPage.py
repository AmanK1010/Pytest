from selenium.webdriver.common.by import By

from test1.PageObject import Locator


class RegisterationPage:
    def __init__(self, driver):
        self.txt_fname = driver.find_element(By.NAME, Locator.first_name_name)
        self.txt_sname = driver.find_element(By.NAME, Locator.sur_name_name)

    def getTxtFName(self):
        return self.txt_fname

    def getTxtSName(self):
        return self.txt_sname
