import allure
from projects import Projects
from tasks import Tasks
from companies import Companies


@allure.id("UI-1")
@allure.feature("CREATE-1")
@allure.title("Тестирование добавления новой компании")
def test_add_company(driver):
    comp = Companies(driver)
    comp.get_page()
    comp.add_company("Новая компания")
    comp.my_company_page()
    comp.get_page()
    res = comp.find_company("Новая компания")
    assert len(res) > 0
    comp.my_company_page()


@allure.id("UI-2")
@allure.feature("CREATE-2")
@allure.title("Тестирование добавления нового проекта")
def test_add_project(driver):
    prjct = Projects(driver)
    prjct.add_project("Тестовый проект")
    title = prjct.get_title()
    prjct.delete_project()
    assert title == "Тестовый проект"


@allure.id("UI-3")
@allure.feature("DELETE-2")
@allure.title("Тестирование удаления нового проекта")
def test_delete_project(driver):
    prjct = Projects(driver)
    prjct.add_project("Тестовый проект")
    len1 = prjct.get_number_of()
    prjct.delete_project()
    len2 = prjct.get_number_of()
    assert len1 - len2 == 1


@allure.id("UI-4")
@allure.feature("CREATE-2.2")
@allure.title("Тестирование добавления новой зачачи")
def test_add_task(driver):
    prjct = Projects(driver)
    prjct.add_project("Проект2")
    prjct.open_project()
    task = Tasks(driver)
    task.add_task("Задача")
    title = task.get_task_title()
    print(title)
    assert title == "Задача"
    task.get_page()
    prjct.delete_project()


@allure.id("UI-5")
@allure.feature("DELETE-2.2")
@allure.title("Тестирование удаления задачи")
def test_delete_task(driver):
    prjct = Projects(driver)
    prjct.add_project("Троект")
    prjct.open_project()
    task = Tasks(driver)
    len1 = task.get_number_off()
    task.add_task("задача")
    len2 = task.get_number_off()
    task.delete_task()
    assert len2 - len1 == 1
