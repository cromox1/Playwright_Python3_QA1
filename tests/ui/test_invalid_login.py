from pages.login_page import LoginPage
from pages.users_page import UsersPage
from utils.json_reader import get_user


def notlogin_page_then_validate(page, list_users):
    for user in list_users:
        login_page = LoginPage(page)
        login_page.open()
        login_page.login(user.username, user.password)
        # Deliberately incorrect expectation
        assert "/users" not in page.url
        assert "/login" in page.url
        users_page = UsersPage(page)
        users_page.verify_user_fail_login()


def test_invalid_login_cred_notexist(page):
    notlogin_page_then_validate(page, [get_user('invalid_user')])

def test_invalid_login_cred_verylong(page):
    notlogin_page_then_validate(page, [get_user('verylong_user'), get_user('verylong_pswd')])

def test_invalid_login_cred_tooshort(page):
    notlogin_page_then_validate(page, [get_user('tooshort_user'), get_user('tooshort_pswd')])

def test_invalid_login_cred_onechar(page):
    notlogin_page_then_validate(page, [get_user('onechar_user'), get_user('onechar_pswd')])

def test_invalid_login_cred_blank(page):
    notlogin_page_then_validate(page, [get_user('blank_user'), get_user('blank_pswd')])
