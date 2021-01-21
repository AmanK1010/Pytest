import pytest

from test1.PageObject.pages.LoginPage import LoginPage
from test1.libglobal.LibGlobal import Base


class TestEmployee(Base):
    @pytest.fixture()
    def setup(self):
        self.driver = self.launch_browser()
        self.loadurl("https://www.facebook.com/")
        yield
        self.quit_browser()

    @pytest.mark.parametrize("username,password",
                             [("abu", "abu@gmail.com")])
    def test_login(self, setup, username, password):
        l = LoginPage(self.driver)
        self.type(l.getTxtUserName(), username)

        self.type(l.getTxtPassword(), password)
        self.btn_click(l.getBtnLogin())
