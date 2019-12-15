from time import sleep
import pytest
from tools.ui.base_ui import BaseUI


@pytest.fixture(scope="session")
def driver():
    driver = BaseUI()
    driver.start_browser()
    driver.get('http://qa.yansl.com/#/login')
    sleep(1)
    # 点击登录
    driver.click("(//span[contains(text(),'登录')])[1]")
    sleep(1)
    # 取消弹框
    driver.click("(//span[contains(text(),'残忍拒绝')])")
    sleep(1)
    # 重新点击登录
    driver.click("(//span[contains(text(),'登录')])[1]")
    sleep(1)
    yield driver
    # 关闭浏览器
    driver.quit()
