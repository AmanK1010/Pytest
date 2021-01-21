from libglobal.LibGlobal import Base
from PageObject.pages.LoginPage import LoginPage


class Employee(Base):
    def login(self):
        driver = self.browser_launch()
        self.load_url("https://www.facebook.com/")
        l = LoginPage(driver)
        self.fill(l.getTxtUserName(), "1234567")
        self.fill(l.getTxtPassword(), "Hello@123")
        self.btn_click(l.getBtnLogin())
        self.quit_browser()


e = Employee()
e.login()
