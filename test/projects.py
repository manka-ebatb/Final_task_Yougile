import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


@allure.epic("YouGile")
class Projects:
    def __init__(self, driver):
        """Инициализация"""
        self._driver = driver
        self._waiter = WebDriverWait(driver, 10)

    @allure.step("Перейти на страницу регистрации")
    def get_login_page(self):
        """Метод позволяет перейти на страницу для регистрации Yougile"""
        self._driver.get("https://www.yougile.com/team/")

    @allure.step("Зарегистрироваться с данными {login} и {password}")
    def auth(self, login: str, password: str):
        """Метод позволяет войти в аккаунт Yougile
        с данными, принимаемыми в переменных"""
        self._waiter.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[type='email']"))
            )
        self._driver.find_element(By.CSS_SELECTOR,
                                  "[type='email']").send_keys(login)
        self._driver.find_element(By.CSS_SELECTOR,
                                  "[type='password']").send_keys(password)
        self._driver.find_element(By.CSS_SELECTOR, "[role='button']").click()

    @allure.step("Добавить проект с названием {name}")
    def add_project(self, name: str):
        """Метод позволяет добавлять проект
        с названием, принимаемым в аргумент"""
        element = "//span[text()='Добавить проект с задачами']"
        self._waiter.until(
            EC.element_to_be_clickable((By.XPATH, element))).click()
        project_name = '//input[@placeholder="Введите название проекта…"]'
        self._driver.find_element(By.XPATH,
                                  project_name).send_keys(name)
        button_add = '//div[./div[text()="Добавить проект с задачами"]]'
        self._driver.find_element(By.XPATH, button_add).click()

    @allure.step("Сменить название последнего проекта на {new_name}")
    def change_project(self, new_name):
        """Метод позволяет изменить название последнего созданного проекта
          на то, которое прописано в аргументе"""
        self._driver.find_elements(By.CSS_SELECTOR, "svg.text-grey")[0].click()
        change = '//div[./div[text()="Переименовать"]]'
        project_name = '//input[@placeholder="Введите название проекта…"]'
        self._driver.find_element(By.XPATH, change).click()
        self._waiter.until(
            EC.presence_of_element_located((By.XPATH, project_name)))
        t_input = self._driver.find_element(By.XPATH, project_name)
        t_input.clear()
        t_input.send_keys(new_name)
        t_input.send_keys(Keys.ENTER)

    @allure.step("Удалить последний созданный проект")
    def delete_project(self):
        """Метод позволяет удалить последний созданный проект"""
        self._driver.find_elements(By.CSS_SELECTOR, "svg.text-grey")[0].click()
        delete = '//div[./div[text()="Удалить"]]'
        self._driver.find_element(By.XPATH, delete).click()
        question = '//div[./div[text()="Отмена"]]'
        self._waiter.until(
            EC.element_to_be_clickable((By.XPATH, question)))
        delete1 = '//div[@role="button"]/div[text()="Удалить"]'
        self._driver.find_element(By.XPATH, delete1).click()
        self._waiter.until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "spinner")))

    @allure.step("Получить количество проектов")
    def get_number_of(self):
        """Метод позволяет получить количество проектов"""
        n = self._driver.find_elements(By.CSS_SELECTOR,
                                       '[data-testid="project-card"]')
        return len(n)

    @allure.step("Открыть последний созданный проект")
    def open_project(self):
        """Метод позволяет перейти в последний созданный проект"""
        p_ct = self._driver.find_elements(By.CSS_SELECTOR,
                                          '[data-testid="project-card"]')[0]
        p_ct.click()

    @allure.step("Получить название последнего проекта")
    def get_title(self) -> str:
        """Метод возвращет имя последнего созданного проекта"""
        res = self._driver.find_elements(By.CSS_SELECTOR,
                                         "[data-testid = 'project-title']")[0]
        return res.text
