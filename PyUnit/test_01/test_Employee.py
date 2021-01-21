import pytest

from test_01.PageObjectModel.Pages.LoginPage import LoginPage
from test_01.libglobal.LibGlobal import Base


class TestEmployee(Base):
    @pytest.yield_fixture()
    def setup(self):
        self.driver = self.launch_browser()
        self.loadurl("https://www.facebook.com/")
        yield
        self.quit_browser()

    @pytest.mark.parametrize("username,password", [("abu", "abu@gmail.com"), ("bala", "bala@gmail.com")])
    def test_login(self, setup, username, password):
        l = LoginPage(self.driver)
        self.type(l.getTxtUserName(), username)
        self.type(l.getTxtPassword(), password)
        self.btn_click(l.getBtnLogin())

    @pytest.mark.xfail
    def test_payment(self):
        print("payment")
        assert 1 == 2
