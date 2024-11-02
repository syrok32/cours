from abc import ABC, abstractmethod


class Get_api_hh(ABC):

    @abstractmethod
    def get_api_rest(self):
        pass


class AbstractFile(ABC):

    @abstractmethod
    def add_vacancy(self, vacancy_data: dict):

        pass

    @abstractmethod
    def get_vacancies(self, **criteria):

        pass

    @abstractmethod
    def delete_vacancy(self, vacancy_name: str):

        pass
