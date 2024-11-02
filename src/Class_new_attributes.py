import json


class Class_main_write:
    """ДОбовление и проверка данных"""

    items_json = {"items": []}
    __slots__ = (
        "__vacancy_name",
        "__vacancy_link",
        "__vacancy_salary",
        "__vacancy_city",
    )

    def __init__(self, vacancy_name, vacancy_link, vacancy_salary, vacancy_city):
        self.__vacancy_name = self.__validate_name(vacancy_name)
        self.__vacancy_link = self.__validate_link(vacancy_link)
        self.__vacancy_salary = self.__validate_salary(vacancy_salary)
        self.__vacancy_city = vacancy_city

    @staticmethod
    def __validate_name(name: str) -> str:
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Название вакансии должно быть непустой строкой.")
        return name

    @staticmethod
    def __validate_link(link: str) -> str:
        if not isinstance(link, str) or not link.startswith("http"):
            raise ValueError("Ссылка на вакансию должна быть строкой, начинающейся с 'http'.")
        return link

    @staticmethod
    def __validate_salary(salary: int) -> int:
        if not isinstance(salary, int) or salary < 0:
            return 0
        elif salary is None:
            return 0
        return salary

    @classmethod
    def __new_vacancy(cls, data_vacancy):
        return cls(**data_vacancy)

    @classmethod
    def __verify_data(self, other):
        if not isinstance(other, (int, Class_main_write)):
            raise TypeError("Операнд справа должен иметь тип int или Class_main_write")

        return other if isinstance(other, int) else other.__vacancy_salary

    def __eq__(self, other):
        salary_div = self.__verify_data(other)
        return self.__vacancy_salary == salary_div

    def __lt__(self, other):
        salary_div = self.__verify_data(other)
        return self.__vacancy_salary < salary_div

    def items_list(self) -> None:
        """Добавляет данные вакансии в общий словарь items_json."""
        Class_main_write.items_json["items"].append(
            {
                "name": self.__vacancy_name,
                "link": self.__vacancy_link,
                "salary": self.__vacancy_salary,
                "city": self.__vacancy_city,
            }
        )

    @classmethod
    def process_vacancies(cls, vacancies):
        """
        Итерирует по списку вакансий, создаёт экземпляр для каждой вакансии,
        добавляет её в items_json и сохраняет в файл.
        """
        for vacancy_data in vacancies:
            vacancy = cls(**vacancy_data)
            vacancy.items_list()
