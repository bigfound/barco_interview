from lib.locators import MainPageLocators
from lib.element import WarrantyPageElement
# from lib.element import BasePageElement
import logging


logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s.%(msecs)03d] %(levelname)s %(filename)s(line:%(lineno)d): %(message)s')


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

    def open_web_page(self, url):
        self.driver.get(url)
        # self.driver.set_window_size(1024, 768)
        self.driver.set_window_position(0, 0)
        self.driver.maximize_window()


class WarrantyPage(BasePage):
    """
    Page related operation
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.h = WarrantyPageElement(self.driver)

    def open_page(self, url):
        self.open_web_page(url)

    def wait_until_home_page(self):
        return self.h.presence_wait_until_find_element(MainPageLocators.main_page)

    def save_screen_shot(self, file_path):
        return self.driver.save_screenshot(file_path)

    def input_sn_and_click_get_info_button(self, serial_number):
        self.h.enter_text_in_text_element(MainPageLocators.serial_number_section, serial_number)

    def get_serial_number_field_value(self):
        return self.h.get_text_element_value(MainPageLocators.serial_number_section)

    def get_warranty_result_items(self):
        warranty_items = []
        warranty_info_element = self.h.get_warranty_info_element(MainPageLocators.warranty_info)
        warranty_info_items_element = self.h.get_warranty_info_items_element(warranty_info_element)
        for warranty_item_element in warranty_info_items_element:
            warranty_items.append(warranty_item_element.text)
        return warranty_items

    def warranty_result_screenshot(self, saved_file_path):
        warranty_info_element = self.h.get_warranty_info_element(MainPageLocators.warranty)
        return warranty_info_element.screenshot(saved_file_path)

    def wait_util_find_all_element(self, element):
        return self.h.visibility_wait_until_find_all_elements(element)


















