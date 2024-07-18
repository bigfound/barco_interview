from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """
    the locators for https://www.barco.com/en/support/clickshare-extended-warranty/warranty
    """
    main_page = (By.TAG_NAME, "body")
    serial_number_section = (By.ID, 'serial')
    warranty_info = (By.CSS_SELECTOR, 'dl.pt-5.cmp-product-warranty__list')

    # for screenshot use
    warranty = (By.XPATH, '//*[@id="warranty"]/div/div[2]/div/div')

    # installation_date = (By.XPATH, "//dl[contains(@class, 'pt-5 cmp-product-warranty__list')]/dd[3]")
    # installation_date = (By.CSS_SELECTOR, 'dl.pt-5.cmp-product-warranty__list dd:nth-of-type(2)')
    # warranty_end_date = (By.XPATH, "//dl[contains(@class, 'pt-5 cmp-product-warranty__list')]/dd[4]")





