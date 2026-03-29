import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@allure.epic("YouGile")
class Tasks:
    def __init__(self, driver):
        """Инициализация"""
        self._driver = driver

    @allure.step("Добавить задачу с названием ")
    def add_task(self, name):
        """Метод позволяет добавить задачу в открытый проект"""
        add = '//div[./span[text()="Добавить задачу"]]'
        self._driver.find_element(By.XPATH, add).click()
        tk = self._driver.find_element(By.CSS_SELECTOR,
                                       "[data-testid='board-task-input-name']")
        tk.send_keys(name, Keys.ENTER)

    @allure.step("Удалить задачу")
    def delete_task(self):
        """Метод позволяет удалять последнюю задачу"""
        param = "[data-testid='board-task-menu']"
        self._driver.find_element(By.CSS_SELECTOR, param).click()
        self._driver.find_element(By.XPATH,
                                  '//div[./div[text()="Удалить"]]').click()
        self._driver.find_element(By.XPATH,
                                  '//div[./div[text()="Удалить"]]').click()

    @allure.step("Получить количество созданных задач")
    def get_number_off(self):
        """Метод позволяет найти количество созданных задач"""
        n = self._driver.find_elements(By.CSS_SELECTOR,
                                       '[data-testid="tw-task-container"]')
        return len(n)

    @allure.step("Получить название задачи")
    def get_task_title(self) -> str:
        """Метод возвращает название задачи"""
        task = "[data-testid='board-task-title']"
        title = self._driver.find_element(By.CSS_SELECTOR, task).text
        return title

    @allure.step("Перейти на страницу с проектами")
    def get_page(self):
        """Метод позволяет перейти на страницу с проектами"""
        self._driver.get("https://www.yougile.com/team/projects")
