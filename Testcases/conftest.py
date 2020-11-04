from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome("Resources/webdriver/chromedriver.exe")

    elif browser == 'firefox':
        driver = webdriver.Firefox(
            executable_path="C:\\Users\\Sanket\\Desktop\\frameworksmyself\\Nopcommerece_Hybrid\\Resources\\webdriver\\geckodriver")
    elif browser == 'cf':

        chrome = webdriver.Chrome("Resources/webdriver/chromedriver.exe")
        firfox = webdriver.Firefox(
            executable_path="C:\\Users\\Sanket\\Desktop\\frameworksmyself\\Nopcommerece_Hybrid\\Resources\\webdriver\\geckodriver")
        list = ['chrome', firfox]
        for i in list:
            driver = i

    else:
        driver = webdriver.Chrome("Resources/webdriver/chromedriver.exe")
    return driver


def pytest_addoption(parser):  # this will get the value from CLT/hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # this will return the browser value to setup method
    return request.config.getoption("--browser")


######### pytest html report ########
#
#  it is hook for adding environment into to HTML Report
def pytest_configure(config):
    config._metadata['project Name'] = 'nop commerce'
    config._metadata['Module Name'] = 'custmer'
    config._metadata['project tester'] = 'Amol'


# It is hook for delete /modify environment info to Html Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("java_home", None)
    metadata.pop("Plugins", None)
