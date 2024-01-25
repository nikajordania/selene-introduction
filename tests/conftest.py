# from webbrowser import Chrome
from webbrowser import Chrome

import pytest
from selene import Browser, Config
from selene.support import shared
from selene import browser, by, be, have
from selene.support.shared import config
from selene.support.shared.jquery_style import s, ss
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(scope='session')
def driver():
    browser = Browser(
        Config(
            driver=webdriver.Edge(service=Service(EdgeChromiumDriverManager().install())),
            timeout=2,
        )
    )
    browser.config.base_url = 'https://google.com'

    yield browser

    browser.quit()


# @pytest.fixture(scope='session', autouse=True)
# def driver_global():
#     custom_url = "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/"
#
#
#     config.browser = Browser(
#         Config(
#             driver=webdriver.Chrome(service=Service(executable_path=r"C:\Users\nika\.wdm\drivers\chromedriver\win64\121.0.6167.85\chromedriver-win32\chromedriver.exe")),
#             timeout=2,
#         )
#     )
#     config.base_url = 'https://google.com'
#
#     yield
#
#     browser.quit()
