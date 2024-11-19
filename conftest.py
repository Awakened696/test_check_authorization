import pytest
from selenium import webdriver
import json

@pytest.fixture(scope='session')
def config():
    with open('config.json') as config_file:
        data = json.load(config_file)
    return data


@pytest.fixture()
def browser(config):

    if config['browser'] == 'chrome':
        driver = webdriver.Chrome()
    elif config['browser'] == 'firefox':
        driver = webdriver.Firefox()
    elif config['browser'] == 'edge':
        driver = webdriver.Edge()
    else:
        raise Exception(f'"{config["browser"]}" is not a supported browser')

    driver.implicitly_wait(config['wait_time'])

    yield driver

    driver.quit()
