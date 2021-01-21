from selenium import webdriver


class Base:
    def launch_browser(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\Vel\PycharmProjects\Adactin\Driver\chromedriver.exe")
        self.driver.maximize_window()
        return self.driver

    def loadurl(self, url):
        self.driver.get(url)

    def quit_browser(self):
        self.driver.quit()

    def type(self, ele, data):
        ele.send_keys(data)

    def btn_click(self, e):
        e.click()
