from selene.support.shared import browser
from selene import be, have


def test_google_search_positive():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_google_search_negative():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('траливалитраливаитратта;').press_enter()
    browser.element('#botstuff').should(have.text('По запросу траливалитраливаитратта; ничего не найдено.'))