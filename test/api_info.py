import requests
import allure
token = "6fTNfeX541vDM42lTNBp6wOo9aBAzPVRma5KwEKrkV0z22fOPd-VSHUGbMfiqVE4"
auth = {"Authorization": f"Bearer {token}"}


@allure.epic("YouGile")
class Api:
    def __init__(self, url) -> None:
        """Инициализация"""
        self.url = url

    @allure.step("Получить список проектов")
    def get_project_list(self):
        """Метод позволяет получить список проектов"""
        list1 = requests.get(self.url + "/api-v2/projects", headers=auth)
        return list1

    @allure.step("Создать проект с названием {name}")
    def create_project(self, name):
        """Метод позволяет создавать проект с названием,
          заданным в переменной"""
        project = {'title': f'{name}'}
        new_project = requests.post(self.url + "/api-v2/projects",
                                    json=project, headers=auth)
        return new_project

    @allure.step("Получить список досок")
    def get_board_list(self):
        """Метод позволяет получить список созданных досок"""
        list = requests.get(self.url + "/api-v2/boards", headers=auth)
        return list

    @allure.step("Создать доску с названием {name} в проексте с id {project}")
    def create_board(self, name, project):
        """Метод позволяет создать доску в проекте"""
        board = {'title': f'{name}',
                 'projectId': f'{project}'}
        new_board = requests.post(self.url + "/api-v2/boards",
                                  json=board, headers=auth)
        return new_board

    @allure.step("Изменить у доски с id {board_id} название на {name}")
    def change_board(self, name, board_id):
        """Метод позволяет изменить созданную доску"""
        board = {'title': f'{name}'}
        change = requests.put(self.url + "/api-v2/boards/" + board_id,
                              json=board, headers=auth)
        return change
