from tools.ui.base_ui import BaseUI


class LoginPage(BaseUI):
    # 登录页面网址
    url = 'http://qa.yansl.com/#/login'
    # 用户名输入框
    p_username = "name=>username"
    # 密码输入框
    p_password = "name=>password"
    # 登录按钮
    p_login = "xpath=>(//span[contains(text(),'登录')])[1]"
    # 残忍拒绝按钮
    p_reject = "xpath=>(//span[contains(text(),'残忍拒绝')])"

    def m_open(self):
        self.get(self.url)

    def m_username(self, username):
        self.send_keys(self.p_username, username)

    def m_password(self, password):
        self.send_keys(self.p_password, password)

    def m_login(self):
        self.click(self.p_login)

    def m_reject(self):
        self.click(self.p_reject)
