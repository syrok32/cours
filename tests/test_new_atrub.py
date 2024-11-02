import pytest

from src.Class_new_attributes import Class_main_write
from src.Class_Vacancy import Vacancy


def test_validate_name():

    assert Class_main_write._Class_main_write__validate_name("Software Engineer") == "Software Engineer"

    with pytest.raises(ValueError):
        Class_main_write._Class_main_write__validate_name("")


def test_validate_link():

    assert Class_main_write._Class_main_write__validate_link("http://example.com") == "http://example.com"

    with pytest.raises(ValueError):
        Class_main_write._Class_main_write__validate_link("example.com")


def test_validate_salary():

    assert Class_main_write._Class_main_write__validate_salary(5000) == 5000

    assert Class_main_write._Class_main_write__validate_salary(-1) == 0
    assert Class_main_write._Class_main_write__validate_salary(None) == 0


def test_items_list():

    vacancy = Class_main_write("Data Scientist", "http://example.com/job/2", 7000, "San Francisco")
    vacancy.items_list()

    assert len(Class_main_write.items_json["items"]) > 0
    assert Class_main_write.items_json["items"][-1] == {
        "name": "Data Scientist",
        "link": "http://example.com/job/2",
        "salary": 7000,
        "city": "San Francisco",
    }


def test_comparison():

    vacancy1 = Class_main_write("Data Scientist", "http://example.com/job/2", 7000, "San Francisco")
    vacancy2 = Class_main_write("Software Engineer", "http://example.com/job/1", 5000, "New York")

    assert vacancy1 > vacancy2
    assert vacancy2 < 6000
    assert vacancy1 == 7000


def test_initialization():

    vacancy = Vacancy("Data Scientist", "http://example.com/job/2", 7000, "San Francisco")

    assert vacancy.vacancy_name == "Data Scientist"
    assert vacancy.vacancy_link == "http://example.com/job/2"
    assert vacancy.vacancy_salary == 7000
    assert vacancy.vacancy_city == "San Francisco"


def test_reper_to_dict():
    vacancy = Vacancy("Software Engineer", "http://example.com/job/1", 5000, "New York")
    result = vacancy.reper_to_dict()

    expected_result = {
        "vacancy_name": "Software Engineer",
        "vacancy_link": "http://example.com/job/1",
        "vacancy_salary": 5000,
        "vacancy_city": "New York",
    }
    assert result == expected_result
