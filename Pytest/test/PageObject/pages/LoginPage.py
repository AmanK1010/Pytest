from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.txt_username = driver.find_element(By.ID, Locator.username_id)
        self.txt_password = driver.find_element(By.ID, Locator.password_id)
        self.btn_login = driver.find_element(By.XPATH, Locator.btn_login_xpath)
        self.btn_create = driver.find_element(By.XPATH, Locator.btn_create_xpath)

    # getters
    def getTxtUserName(self):
        return self.txt_username

    def getTxtPassword(self):
        return self.txt_password

    def getBtnLogin(self):
        return self.btn_login

    def getBtnCreateNew(self):
        return self.btn_create
