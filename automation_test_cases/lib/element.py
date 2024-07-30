from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import logging

logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s.%(msecs)03d] %(levelname)s %(filename)s(line:%(lineno)d): %(message)s')


class BasePageElement(object):
    """
    Page elements related operation

    """
    def __init__(self, driver):
        self.driver = driver

    def presence_wait_until_find_element(self, element, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(element))

    def visibility_wait_until_find_all_elements(self, element, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(element))

    def presence_wait_until_find_all_elements(self, element, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(element))

    def click_element(self, element):
        if not self.visibility_wait_until_find_all_elements(element):
            logging.error('Cannot find the element to click: {}'.format(element))
            return -1
        o = self.driver.find_element(element[0], element[1])
        logging.info('Click the element: {}'.format(element))
        o.click()

    def enter_text_in_text_element(self, element, text):
        if not self.visibility_wait_until_find_all_elements(element):
            logging.error('Cannot find the element to input text: {}'.format(element))
            return -1
        text_field = self.driver.find_element(element[0], element[1])
        logging.info('Click the element: {}'.format(element))
        text_field.send_keys(text)
        text_field.send_keys(Keys.RETURN)

    def get_text_element_value(self, element):
        if not self.visibility_wait_until_find_all_elements(element):
            logging.error('Cannot find the text element: {}'.format(element))
            return -1
        text_element = self.driver.find_element(element[0], element[1])
        return text_element.get_attribute('value')


class WarrantyPageElement(BasePageElement):
    """
    Page elements related operation

    """

    def __init__(self, driver):
        super().__init__(driver)

    def get_warranty_info_element(self, element):
        """
        the format for warranty info element:
        <dl class="pt-5 cmp-product-warranty__list">
            <dt class>Description</dt>
            <dd class>CLICKSHARE CX-50 SET NA</dd>
            <dt class>Part number</dt>
            <dd class>R9861522NA</dd>
            <dt class>Installation date</dt>
            <dd class>28 September 2020</dd>
            <dt class>Warranty end date</dt>
            <dd class="">27 September 2021</dd>
        </dl>
        """
        if not self.visibility_wait_until_find_all_elements(element):
            logging.error('Cannot find the element to get warranty info: {}'.format(element))
            return -1
        return self.driver.find_element(element[0], element[1])

    def get_warranty_info_items_element(self, warranty_info_element):
        """
        example:
        warranty_info_element = self.h.get_warranty_info_element(MainPageLocators.warranty_info)
        warranty_info_items_element_list = self.h.get_warranty_info_items_element(warranty_info_element)

        """
        return warranty_info_element.find_elements(By.XPATH, './dt')











