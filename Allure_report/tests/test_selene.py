from selene.support.shared import browser

def test_github():
    browser.open('https://github.com')

    s('.header-search-input').click()
    s('.header-search-input').send_keys("eroshenkoam/allure-example")
    s('.header-search-input').submit()

    s(by.link_text(eroshenko/allure-example)).click()

    s("#issue-tab").click()
    s(by.partial_text("#76")).should(be.visible)
