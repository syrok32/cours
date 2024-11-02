import json
from typing import Dict

from src.abstraction_class import AbstractFile


class JSONFileHandler(AbstractFile):
    "запись новых вакансий в файл"

    def __init__(self, filename):
        self.filename = filename

        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = {"items": []}
            self.save_data()

    def save_data(self) -> None:
        """Сохрпнение в файл"""

        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(self.data, file, ensure_ascii=False, indent=4)

    def add_vacancy(self, vacancy_data: dict):
        """Добовление в новых вакансий"""
        self.data["items"].append(vacancy_data)
        self.save_data()

    def get_vacancies(self, **criteria) -> Dict:
        """поиск по клюсам"""
        result = self.data["items"]
        for key, value in criteria.items():
            result = [vacancy for vacancy in result if vacancy.get(key) == value]
        return result

    def delete_vacancy(self, vacancy_name: str):
        """удвлвние проекта"""

        self.data["items"] = [vacancy for vacancy in self.data["items"] if vacancy.get("name") != vacancy_name]
        self.save_data()
