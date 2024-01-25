from webbrowser import Chrome

from selene import browser, by, be, have, Browser, Config, query
from selene.support import shared
from selenium.webdriver.common.by import By


def test_selene_introduction(driver):
    driver.open('/ncr')
    # browser.element(by.name('q')).should(be.blank)\
    #     .type('selenium').press_enter()
    # browser.all('#rso>div').should(have.size_greater_than(5))\
    #     .first.should(have.text('Selenium automates browsers'))


def test_selene_global_config():
    browser.open('/ncr')
    # browser.element(by.name('q')).should(be.blank)\
    #     .type('selenium').press_enter()
    # browser.all('#rso>div').should(have.size_greater_than(5))\
    #     .first.should(have.text('Selenium automates browsers'))


from selene.api import s, ss


def test_handle_dynamic_table():
    browser.open('http://techcanvass.com/Examples/webtable.html').open()

    web_table = s('//table')
    rows = web_table.all('.//tr')
    print("Number of Rows including headings:", len(rows))

    columns = rows[0].all('.//th')
    print("Number of columns:", len(columns))

    for r_num in range(1, len(rows) + 1):
        for col_num in range(1, len(columns) + 1):
            if r_num == 1:
                cell_text = s(f".//*[@id='t01']/tbody/tr[{r_num}]/th[{col_num}]").get(query.text)
            else:
                cell_text = s(f".//*[@id='t01']/tbody/tr[{r_num}]/td[{col_num}]").get(query.text)

            print(cell_text)


def test_implicit_wait():
    browser.open("http://the-internet.herokuapp.com/")
    browser.config.timeout = 10
    dynamic_controls_page = browser.element(by.css("li a[href='/dynamic_controls']"))
    dynamic_controls_page.click()

    checkbox = browser.element(by.css("form#checkbox-example #checkbox > input[type=checkbox]"))
    checkbox.click()

    # assert element.is_selected() is True
    assert checkbox.should(be.selected)

    browser.element(by.css("#checkbox-example > button")).click()
    browser.element(by.css("#checkbox-example #message")).should(be.visible)


def test_explicit_wait():
    browser.open("http://the-internet.herokuapp.com/")

    dynamic_controls_page = browser.element(by.css("li a[href='/dynamic_controls']"))
    dynamic_controls_page.click()

    # checkbox = browser.element(by.css("form#checkbox-example #checkbox > input[type=checkbox]"))
    # checkbox.click()

    # webelement = browser.find_element(By.TAG_NAME, 'div')
    # selene_element = s(webelement)

    # assert element.is_selected() is True
    #
    # driver = browser.driver
    # assert checkbox. is True

    element = browser.driver.find_element(By.CSS_SELECTOR, "form#checkbox-example #checkbox > input[type=checkbox]")

    element.click()

    assert element.is_selected() is True

    browser.element(by.css("#checkbox-example > button")).click()

    browser.element("#checkbox-example #message").wait_until(be.visible)

    message = browser.element(by.css("#checkbox-example #message")).get(query.text)
    print(message)
