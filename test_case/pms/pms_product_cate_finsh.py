from test_case.pms.pms_add_product_cate import addProductCate
from test_case.pms.pms_product_cate import ProductCate


def open_product_cate():
    pc = ProductCate()
    pc.m_get_page()


def add_button():
    pc = ProductCate()
    pc.m_click_add_product_cate()


def add_product_cate(cate_name, parent_cate, amount_unit, order_by, is_display, navicate_display, att1, att2, key_word,
                     desc):
    apc = addProductCate()
    apc.m_send_cate_name(cate_name)
    apc.m_choose_parent_cate(parent_cate)
    apc.m_send_amount_unit(amount_unit)
    apc.m_send_order_by(order_by)
    apc.m_click_display(is_display)
    apc.m_click_navicate_display(navicate_display)
    # apc.m_upload(icon)
    apc.m_choose_attribute(att1, att2)
    apc.m_send_key_words(key_word)
    apc.m_send_cate_desc(desc)
    apc.m_click_submit()
    apc.m_click_accept()
