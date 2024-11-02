import json
from typing import Any


class Class_main:
    """Перезапись в новый файл с нужными параметрами"""

    def open_json_get(self) -> dict:
        """Запись в новый файл"""
        with open("./json_vacancy.json", "r", encoding="utf-8") as file:
            return json.load(file)

    def create_sort(self) -> list[dict[str, Any | None]]:
        """Запись только  нужных даннных"""
        answer_dict = self.open_json_get().get("items")
        vacancies = []
        for i in answer_dict:
            vacancies.append(
                {
                    "vacancy_name": i.get("name"),
                    "vacancy_link": i.get("apply_alternate_url"),
                    "vacancy_salary": (i.get("salary").get("from") if i.get("salary") else None),
                    "vacancy_city": i.get("area").get("name"),
                }
            )
        return vacancies
