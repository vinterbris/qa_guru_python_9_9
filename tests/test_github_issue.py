import allure
from allure_commons.types import Severity
from selene import by, have
from selene.support.shared import browser


def test_pure_selene():
    browser.open('/')

    browser.element(".header-search-button").click()
    browser.element("#query-builder-test").type("qa-guru/knowledge-base")
    browser.element("#query-builder-test").submit()

    browser.element(by.link_text("qa-guru/knowledge-base")).click()

    browser.element("#issues-tab").click()

    browser.element('#issue_3_link').should(
        have.exact_text("Plain value cannot start with reserved character ` at line 1, column 10"))


@allure.title("Test Issue name")
@allure.description("This test attempts to check name of the issue. Fails if any error happens."
                    "\n\nNote that this description is just a test of allure capabilities.")
@allure.tag("Issue", "Essentials", "Github", 'QA.GURU')
@allure.severity(allure.severity_level.NORMAL)
@allure.label("owner", "Sergey Dobrovolskiy")
@allure.link("https://dev.example.com/", name="Website")
@allure.issue("GTH-123")
@allure.testcase("TMS-456")
@allure.parent_suite("Tests for web interface")
@allure.suite("Tests for essential features")
@allure.sub_suite("Tests for issue name 1")
@allure.epic("github")
@allure.feature("Задачи в репозитории")
@allure.story("Имя задачи корректно")
def test_with_allure_step():
    with allure.step('Открываем главную страницу'):
        browser.open('/')

    with allure.step('Ищем репозиторий'):
        browser.element(".header-search-button").click()
        browser.element("#query-builder-test").type("qa-guru/knowledge-base")
        browser.element("#query-builder-test").submit()

    with allure.step('Открываем репозиторий по ссылке'):
        browser.element(by.link_text("qa-guru/knowledge-base")).click()

    with allure.step('Переходим на вкладку issues'):
        browser.element("#issues-tab").click()

    with allure.step('Проверяем название Issue'):
        browser.element('#issue_3_link').should(
            have.exact_text("Plain value cannot start with reserved character ` at line 1, column 10"))


@allure.title("Test Issue name")
@allure.description("This test attempts to check name of the issue. Fails if any error happens."
                    "\n\nNote that this description is just a test of allure capabilities.")
@allure.tag("Issue", "Essentials", "Github", 'QA.GURU')
@allure.severity(allure.severity_level.MINOR)
@allure.label("owner", "Sergey Dobrovolskiy")
@allure.link("https://dev.example.com/", name="Website")
@allure.issue("GTH-123")
@allure.testcase("TMS-456")
@allure.parent_suite("Tests for web interface")
@allure.suite("Tests for essential features")
@allure.sub_suite("Tests for issue name 2")
def test_decorator_allure_step():
    open_main_page()
    find_repository("qa-guru/knowledge-base")
    open_repository("qa-guru/knowledge-base")
    open_issues_tab()
    check_issue_name("Plain value cannot start with reserved character ` at line 1, column 10")


@allure.step('Открываем главную страницу')
def open_main_page():
    browser.open('/')


@allure.step('Ищем репозиторий')
def find_repository(repo):
    browser.element(".header-search-button").click()
    browser.element("#query-builder-test").type(repo)
    browser.element("#query-builder-test").submit()


@allure.step('Открываем репозиторий по ссылке')
def open_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step('Переходим на вкладку issues')
def open_issues_tab():
    browser.element("#issues-tab").click()


@allure.step('Проверяем название Issue')
def check_issue_name(text):
    browser.element('#issue_3_link').should(
        have.exact_text(text))
