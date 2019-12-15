from test_case.pms.pms_product_cate_finsh import *


def test_add_product_cate(driver):
    open_product_cate()
    add_button()
    cate_name = "夏季体恤"
    parent_cate = "服装"
    amount_unit = "件"
    order = "0"
    display = "是"
    navicate_display = "是"
    att_1 = "服装-裤装"
    att_2 = "风格"
    keys_word = "时尚"
    cate_desc = "随意"
    add_product_cate(cate_name, parent_cate, amount_unit, order, display, navicate_display, att_1, att_2, keys_word,
                     cate_desc)
