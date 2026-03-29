import allure
from api_info import Api


api = Api("https://ru.yougile.com")


@allure.id("API-1")
@allure.feature("CREATE-1")
@allure.title("Тестирование добавления проекта")
def test_create_project():
    new_project = api.create_project("Имя проекта")
    assert new_project.status_code == 201


@allure.id("API-2")
@allure.feature("CREATE-2")
@allure.title("Тестирование получения списка проектов")
def test_get_project_list():
    projects = api.get_project_list()
    assert projects.status_code == 200


@allure.id("API-3")
@allure.feature("CREATE-1.2")
@allure.title("Тестирование добавления доски в проект")
def test_create_board():
    project = api.create_project("проект 1")
    p_id = project.json()["id"]
    board = api.create_board("доска 1", p_id)
    assert board.status_code == 201


@allure.id("API-4")
@allure.feature("CREATE-2.2")
@allure.title("Тестирование получения списка задач")
def test_get_board_list():
    boards = api.get_board_list()
    assert boards.status_code == 200


@allure.id("API-5")
@allure.feature("CHANGE-2")
@allure.title("Тестирование редактирования задачи")
def test_change_board():
    project = api.create_project("проект 1")
    p_id = project.json()["id"]
    board = api.create_board("доска 1", p_id)
    b_id = board.json()["id"]
    board1 = api.change_board("доска 2", b_id)
    assert board1.status_code == 200
