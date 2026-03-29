from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from projects import Projects

login = "kon-v-palto-v-paltishke@yandex.ru"
password = "DD4-jDJ-C9H-XPP"


@pytest.fixture(scope="session")
def driver():
    """
    Открывает и настраивает браузер.
    """
    driver = webdriver.Chrome(service=ChromeService
                              (ChromeDriverManager().install()))
    driver.implicitly_wait(30)
    driver.maximize_window()
    prjct = Projects(driver)
    prjct.get_login_page()
    prjct.auth(login, password)
    yield driver

    driver.quit()
