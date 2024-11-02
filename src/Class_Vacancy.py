class Vacancy:
    """для создание новых вакансий"""

    __slots__ = ("vacancy_name", "vacancy_link", "vacancy_salary", "vacancy_city")

    def __init__(self, vacancy_name, vacancy_link, vacancy_salary, vacancy_city):
        self.vacancy_name = vacancy_name
        self.vacancy_link = vacancy_link
        self.vacancy_salary = vacancy_salary
        self.vacancy_city = vacancy_city

    def reper_to_dict(self) -> dict:
        return {
            "vacancy_name": self.vacancy_name,
            "vacancy_link": self.vacancy_link,
            "vacancy_salary": self.vacancy_salary,
            "vacancy_city": self.vacancy_city,
        }
