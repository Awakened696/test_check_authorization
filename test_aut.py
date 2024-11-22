from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException

def test_aut(browser):

    url = 'https://www.saucedemo.com/'
    browser.get(url)

    browser.find_element(By.ID, 'user-name').send_keys('standard_user')

    browser.find_element(By.ID, 'password').send_keys('secret_sauce')

    browser.find_element(By.ID, 'login-button').click()

    try:
        content_check = browser.find_element(By.CLASS_NAME, 'inventory_container')
        assert content_check.is_displayed()
    except NoSuchElementException:
        assert False
