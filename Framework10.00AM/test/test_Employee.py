import pytest

from test_02.PageObject.pages.LoginPage import LoginPage
from test_02.libglobal.LibGlobal import Base


class TestEmployee(Base):

    @pytest.yield_fixture()
    def setup(self):
        driver = self.launch_browser()
        self.loadurl("https://www.facebook.com/")
        yield
        self.quit_browser()

    @pytest.mark.parametrize("username,password",
                             [("abu", "abu@gmail.com"), ("mani", "mani@gmail.com"), ("guna", "guna@gmail.com")])
    def test_login(self, setup, username, password):
        l = LoginPage(self.driver)
        self.type(l.getTxtUserName(), username)
        self.type(l.getTxtPassword(), password)
        self.btn_click(l.getBtnLogin())
