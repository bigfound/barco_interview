import pytest
import logging
import datetime
import os
import shutil
import allure
from page_urls import warranty_page_url
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from lib.util import create_log_folder
from lib.pages import WarrantyPage
from lib.locators import MainPageLocators
from selenium.common.exceptions import TimeoutException


logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('[%(asctime)s.%(msecs)03d] %(levelname)s %(filename)s(line:%(lineno)d): %(message)s',
                              datefmt='%Y%m%d %H:%M:%S')
log_filename = datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S_console.log")
fh = logging.FileHandler(log_filename)
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
logger.addHandler(fh)


class TestCases:
    @pytest.fixture(scope='class', autouse=True)
    def setup_teardown(self):
        global driver, log_folder
        chrome_driver_path = './chromedriver.exe'
        log_folder = os.path.join(os.path.dirname(__file__), "log")
        create_log_folder(log_folder)
        service = Service(chrome_driver_path)
        driver = webdriver.Chrome(service=service)
        yield
        copy_to_log_folder = [log_filename]
        for file in copy_to_log_folder:
            if not os.path.isfile(file):
                pytest.error('Copy the {} to the log folder failed.'.format(file))
            shutil.copyfile(file, os.path.join(log_folder, file))

    @allure.title("Test case: Get warranty result with special characters")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.Warranty_0003
    def test_get_warranty_info_with_special_characters(self):
        """
        Test case name: Warrenty_0003
        Description: Get warranty info with Special characters(!@#$%^&*(_)+_.,/?~)

        """

        special_characters = '!@#$%^&*(_)+_.,/?~'
        logger.info('Step1: go to warranty page')
        logger.info(warranty_page_url)
        warranty_page = WarrantyPage(driver)
        warranty_page.open_page(warranty_page_url)

        if not warranty_page.wait_until_home_page():
            logger.error('Opened warranty page failed.')

        try:
            logger.info('Step2: Press the Get info button with special characters(!@#$%^&*(_)+_.,/?~)')
            warranty_page.input_sn_and_click_get_info_button(special_characters)
            element = warranty_page.wait_util_find_all_element(MainPageLocators.warranty_info)
            assert element is None, 'There should not have any info shows up'
        except TimeoutException:
            logger.info('There is no any shows up after input invalid serial number')
            logger.info('Test result: PASSED')

    @allure.title("Test case: Get warranty info with serial number length = 1/4/5/6")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.Warranty_0005
    def test_get_warranty_info_with_various_number_length(self, various_number_length):
        """

        Test case name: Warranty_0005
        Description: Get warranty info with number length = 1/4/5/6

        expected warranty result output format:

        Description:          CLICKSHARE CX-50 SET NA
        Part number:          R9861522NA
        Installation date:    28 September 2020
        Warranty end date:    27 September 2021

        """
        serial_number = various_number_length
        screenshot = os.path.join(log_folder, 'Warrenty_0005_SN_{}.png'.format(serial_number))

        # as mentioned in "Barco Interview Assignment.pdf", the expected items are below:
        expected_warranty_result_items = ['Description', 'Part number', 'Installation date', 'Warranty end date']
        logger.info('Step1: go to the warranty page')
        logger.info(warranty_page_url)
        warranty_page = WarrantyPage(driver)
        warranty_page.open_page(warranty_page_url)

        if not warranty_page.wait_until_home_page():
            logger.error('Opened warranty page failed.')
        try:
            logger.info('Step2: Press the Get info button with various number length, SN: {}'.format(serial_number))
            warranty_page.input_sn_and_click_get_info_button(serial_number)
            warranty_page.wait_util_find_all_element(MainPageLocators.warranty_info)
            warranty_result_items = warranty_page.get_warranty_result_items()
            logger.info('SN: {}, warranty info items: {}'.format(serial_number, warranty_result_items))

            screenshot_result = warranty_page.warranty_result_screenshot(screenshot)
            if not screenshot_result:
                pytest.fail('Screenshot failed: {}'.format(screenshot))
            logger.info('Completed screenshot')

            assert expected_warranty_result_items == warranty_result_items, \
                'The output format of warranty info is different from the expected items'
        except TimeoutException:
            logger.info('There is no any shows up after input invalid serial number')
            logger.info('Test result: PASSED')

    @allure.title("Test case: Check Web page reload status")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.Warranty_0007
    def test_check_web_page_reload_status(self):
        """
        Test case name: Warrenty_0007
        Description: Check Web page reload status, the text field and info are empty after refreshing the web page

        """
        serial_number = '1863552437'
        logger.info('Step1: go to the warranty page')
        logger.info(warranty_page_url)
        warranty_page = WarrantyPage(driver)
        warranty_page.open_page(warranty_page_url)

        if not warranty_page.wait_until_home_page():
            logger.error('Opened warranty page failed.')

        logger.info('Step2: Press the Get info button with valid SN: {}'.format(serial_number))
        warranty_page.input_sn_and_click_get_info_button(serial_number)
        sn_field_value = warranty_page.get_serial_number_field_value()
        logger.info('serial number field value: {}'.format(sn_field_value))
        logger.info('Step3: Refresh the web page')
        driver.refresh()
        sn_field_value = warranty_page.get_serial_number_field_value()
        logger.info('serial number field value: {}'.format(sn_field_value))
        assert sn_field_value == "", 'The serial number field value should be empty after refreshing the web page'
        logger.info('Test result: PASSED')















