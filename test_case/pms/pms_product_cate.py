from tools.ui.base_ui import BaseUI


class ProductCate(BaseUI):
    url = "http://qa.yansl.com/#/pms/productCate"
    p_add_product_cate = '''//span[contains(text(),'添加') and text() != "添加商品"]'''

    def m_get_page(self):
        self.get(self.url)

    def m_click_add_product_cate(self):
        self.click(self.p_add_product_cate)
