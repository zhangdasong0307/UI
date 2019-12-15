import random
from time import sleep


# 添加下级分类
def test_add_product_cate(driver):
    driver.get("http://qa.yansl.com/#/pms/addProductCate")
    sleep(2)
    # 分类名称输入：夏季T恤你你你你你你你
    driver.send_keys('//label[contains(text(),"分类名称")]/../div//input', "夏季T恤{:0>6d}".format(random.randint(0, 100000)))

    sleep(2)
    # 点击上级分类
    driver.click('//label[contains(text(),"上级分类")]/../div//input')
    sleep(2)
    # 选择服装
    driver.click("//span[text()='服装']")
    sleep(2)
    # 输入数量单位 件
    driver.send_keys('//label[contains(text(),"数量单位")]/../div//input', "件")
    # 选择显示
    driver.click('''//label[contains(text(),"是否显示：")]/../div//span[contains(text(),'是')]/../span/span''')
    sleep(2)
    # 选择导航栏显示
    driver.click('''//label[contains(text(),"是否显示在导航栏")]/../div//span[contains(text(),'是')]/../span/span''')
    sleep(2)
    driver.scroll_screen_x_y(0, 2000)
    sleep(2)
    # 点击提交按钮
    driver.click("//span[text()='提交']")
    sleep(2)
