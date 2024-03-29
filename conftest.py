import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default="Chrome")
    parser.addoption('--language', action='store')


@pytest.fixture(scope='function')
def browser(request):
	browser = request.config.getoption("browser")
	user_language = request.config.getoption("language")
	if (browser == "Chrome"):
		options = Options()
		options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
		browser = webdriver.Chrome(options=options)
	elif (browser == "Firefox"):
		fp = webdriver.FirefoxProfile()
		fp.set_preference("intl.accept_languages", user_language)
		browser = webdriver.Firefox(firefox_profile=fp)
	yield browser
	browser.quit()
