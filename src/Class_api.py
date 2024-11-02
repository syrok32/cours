import json

import requests

from src.abstraction_class import Get_api_hh


class Api_hh(Get_api_hh):
    """Получение json ответва c параметром ключнвого слова и количеством"""

    def __init__(self, serch=None, per_page=10) -> None:
        self.__serch = serch
        self.__per_page = per_page
        url_get = "https://api.hh.ru/vacancies"  # используемый адрес для отправки запроса
        params = {"text": self.__serch, "per_page": self.__per_page}
        self.response = requests.get(url_get, params=params)
        if not self.response.status_code == 200:
            raise TypeError("не верный ствтус код")

    def get_api_rest(self) -> None:
        """Запись в файл временый json"""
        with open("./src/json_vacancy.json", "w", encoding="utf-8") as file:
            json.dump(self.response.json(), file, indent=4, ensure_ascii=False)
