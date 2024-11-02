from src.Class_api import Api_hh
from src.Class_atrub import Class_main
from src.Class_new_attributes import Class_main_write
from src.Class_save import JSONFileHandler
from src.Class_Vacancy import Vacancy

vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", 3500000, "Cheb")

json_saver = JSONFileHandler("./data/vacancies.json")
json_saver.add_vacancy(vacancy.reper_to_dict())


def user_interaction():
    search_query = input("Введите поисковый запрос по ключевым словам: ")

    top_n = int(input("Введите количество вакансий для поиска: "))
    name1 = Api_hh(search_query, top_n)
    name1.get_api_rest()
    emp1 = Class_main()
    print(emp1.create_sort())
    Class_main_write.process_vacancies(emp1.create_sort())
    emp2 = JSONFileHandler("./data/vacancies.json")
    get_vac = int(input("удалить вакансию 1-да 2-нет"))
    if get_vac == 1:
        delet_name = input("Ввидите названия вакансии")  # Программист Python
        json_saver.delete_vacancy(delet_name)
        print("Вакансии после удаления:", json_saver.get_vacancies())

    salary_get = int(input("ввидите зп"))
    if json_saver.get_vacancies(salary=salary_get):
        print(
            f"Вакансии с зарплатой {salary_get}:",
            json_saver.get_vacancies(salary=salary_get),
        )
    else:
        print(f"Вакансии с зарплатой {salary_get}: не найдено")


print(user_interaction())
