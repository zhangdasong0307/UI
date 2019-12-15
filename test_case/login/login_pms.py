from test_case.login.login_page import LoginPage


def user_login(username, pwd):
    login = LoginPage()
    login.m_open()
    login.m_username(username)
    login.m_password(pwd)
    login.m_login()
    login.m_reject()
    login.m_login()
