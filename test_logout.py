from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

def test_logout(browser):

    url = 'https://www.saucedemo.com/'
    browser.get(url)

    browser.find_element(By.ID, 'user-name').send_keys('standard_user')

    browser.find_element(By.ID, 'password').send_keys('secret_sauce')

    browser.find_element(By.ID, 'login-button').click()

    browser.find_element(By.CLASS_NAME, 'bm-burger-button').click()

    browser.find_element(By.LINK_TEXT, 'Logout').click()

    try:
        check_content = browser.find_element(By.CLASS_NAME, 'login_wrapper-inner')
        assert check_content.is_displayed()

    except NoSuchElementException:
        assert False