from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select


class Base:
    def browser_launch(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\Vel\PycharmProjects\Adactin\Driver\chromedriver.exe")
        self.driver.maximize_window()
        return self.driver

    def load_url(self, url):
        self.driver.get(url)

    def fill(self, element, data):
        element.send_keys(data)

    def btn_click(self, element):
        element.click()

    def quit_browser(self):
        self.driver.quit()

    def right_click(self, e):
        acc = ActionChains(self.driver)
        acc.context_click(e).perform()

    def get_text(self, ele):
        t = ele.text
        return t

    def dd_by_index(self, element, index):
        s = Select(element)
        s.select_by_index(index)
