import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#функция для того, чтобы можно было выставить язык в консоли для страницы
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose browser: chrome or firefox")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
#
    yield browser
    print("\nquit browser..")
    browser.quit()
