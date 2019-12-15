from tools.ui.base_ui import BaseUI


class addProductCate(BaseUI):
    p_cate_name = "//label[contains(text(),'分类名称')]/../div//input"
    p_parent_cate = "//label[contains(text(),'上级分类')]/../div//input"
    p_parent_cate_option = "(//ul)[last()]//span[text()='{}']"
    p_amount_unit = "//label[contains(text(),'数量单位')]/../div//input"
    p_order_by = "//label[contains(text(),'排序')]/../div//input"
    p_display = "//label[contains(text(),'是否显示：')]/../div//span[contains(text(),'{}')]/../span[1]"
    p_navicate_display = "//label[contains(text(),'是否显示在导航栏')]/../div//span[contains(text(),'{}')]/../span[1]"
    p_upload = "//span[text()='点击上传']"
    p_attribute = '//label[text()="筛选属性："]/../div//input'
    p_attribute_option_1 = '//ul[contains(@id,"cascader-menu")]/li[contains(text(),"{}")]'
    p_attribute_option_2 = '''//ul[contains(@id,"cascader-menu")]/../ul[2]/li[contains(text(),'{}')]'''
    # p_add_attribute = '//span[text()="新增"]'
    p_key_words = "//label[contains(text(),'关键词')]/../div//input"
    p_cate_desc = "//label[contains(text(),'分类描述')]/../div//textarea"
    p_submit = "//span[contains(text(),'提交')]"
    p_accept = "//span[contains(text(),'确定')]"

    def m_click_accept(self):
        self.click(self.p_accept)

    def m_click_submit(self):
        self.click(self.p_submit)

    def m_send_cate_desc(self, text):
        self.send_keys(self.p_cate_desc, text)

    def m_send_key_words(self, text):
        self.send_keys(self.p_key_words, text)

    # def m_click_add_attribute(self):
    #     self.click(self.p_add_attribute)
    def m_choose_attribute(self, at_1, at_2):
        self.click(self.p_attribute)
        self.click(self.p_attribute_option_1.format(at_1))
        self.click(self.p_attribute_option_2.format(at_2))

    def m_upload(self, file_path):
        self.file_upload(self.p_upload, file_path)

    def m_click_navicate_display(self, is_display):
        self.click(self.p_navicate_display.format(is_display))

    def m_click_display(self, is_display):
        self.click(self.p_display.format(is_display))

    def m_send_order_by(self, text):
        self.send_keys(self.p_order_by, text)

    def m_send_amount_unit(self, text):
        self.send_keys(self.p_amount_unit, text)

    def m_send_cate_name(self, text):
        self.send_keys(self.p_cate_name, text)

    def m_choose_parent_cate(self, option):
        self.click(self.p_parent_cate)
        self.click(self.p_parent_cate_option.format(option))
