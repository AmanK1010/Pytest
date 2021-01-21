import pytest


@pytest.mark.E2E
@pytest.mark.reg
def test_login_facebook():
    print("facebook login")


@pytest.mark.E2E
@pytest.mark.sanity
def test_login_twitter():
    print("twitter login")


@pytest.mark.E2E
@pytest.mark.smoke
def test_login_gmail():
    print("gmail login")
