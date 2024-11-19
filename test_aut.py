from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException

def test_aut(browser):

    url = 'https://www.saucedemo.com/'
    browser.get(url)

    browser.find_element(By.ID, 'user-name').send_keys('standard_user')

    browser.find_element(By.ID, 'password').send_keys('secret_sauce')

    browser.find_element(By.ID, 'login-button').click()

    try:
        browser.find_element(By.CLASS_NAME, 'bm-burger-button').click()
        logout_button = browser.find_element(By.LINK_TEXT, "Logout")
        assert logout_button.is_displayed()
    except NoSuchElementException:
        assert False, "Logout button does not exist."