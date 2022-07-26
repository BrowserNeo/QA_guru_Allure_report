import allure
from selene import by, be
from selene.support.shared import browser



def test_decorator_steps():
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repositiry("eroshenkoam/allure-example")
    open_issues_tab()
    should_see_issue_with_number("76")


@allure.step("Open main page")
def open_main_page():
    browser.open('https://github.com')



@allure.step("Searching of repositories {repo}")
def search_for_repository(repo):
    browser.element('.header-search-input').click()
    browser.element('.header-search-input').send_keys(repo)
    browser.element('.header-search-input').submit()


@allure.step("Go to link repository {repo}")
def go_to_repositiry(repo):
    browser.element(by.link_text(repo)).click()


@allure.step("Open tab Issues")
def open_issues_tab():
    browser.element("#issues-tab").click()


@allure.step("Should see Issue with number {number}")
def should_see_issue_with_number(number):
    number = '#76'
    browser.element(by.partial_text(number)).should(be.visible)

