import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

@allure.epic("YouGile")
class Companies:
    def __init__(self, driver):
        """Инициализация"""
        self._driver = driver
        self._waiter = WebDriverWait(driver, 10)

    @allure.step("Перейти на страницу профиля")
    def get_page(self):
        """Метод позволяет перейти на страницу профиля"""
        loader = ".loader flex flex-col items-center"
        self._waiter.until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, loader)))
        self._driver.get("https://www.yougile.com/team/settings-account")

    @allure.step("Перейти на страницу 'Моя компания'")
    def my_company_page(self):
        """Метод позволяет перейти на страницу приоритетной компании"""
        self._driver.get("https://www.yougile.com/team/projects")

    @allure.step("Добавить компанию с названием {name}")
    def add_company(self, name):
        """Метод позволяет добавить компанию с названием 
        принимаемым в аргумент"""
        button = self._driver.find_element(By.XPATH,
                                           "//div[text()='Добавить компанию']")
        actions = ActionChains(self._driver)
        actions.move_to_element(button).perform()
        self._waiter.until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//div[text()='Добавить компанию']"))
                                        ).click()
        self._driver.find_element(By.CSS_SELECTOR,
                                  ".add-company__input").send_keys(name)
        self._driver.find_element(By.CSS_SELECTOR,
                                  ".add-company__submit").click()
        success = "//span[text()='Компания успешно создана']"
        self._waiter.until(
            EC.visibility_of_element_located((By.XPATH, success)))

    @allure.step("Найти список доваленных компаний с названием {name}")
    def find_company(self, name):
        """Метод возвращает список компаний с названием,
          принимаемым в аргумент"""
        company = f"//div[contains(@class, 'truncate') and text()= '{name}']"
        c_list = self._driver.find_elements(By.XPATH, company)
        return c_list
