import json

import pytest

from src.Class_save import JSONFileHandler


@pytest.fixture
def json_handler(tmp_path):

    file_path = tmp_path / "test_vacancies.json"
    handler = JSONFileHandler(file_path)
    return handler


def test_initialization(json_handler):

    assert json_handler.data == {"items": []}


def test_add_vacancy(json_handler):

    vacancy_data = {
        "name": "Software Engineer",
        "link": "http://example.com/job/1",
        "salary": 5000,
        "city": "New York",
    }
    json_handler.add_vacancy(vacancy_data)
    assert json_handler.data["items"][-1] == vacancy_data

    with open(json_handler.filename, "r", encoding="utf-8") as file:
        data = json.load(file)
        assert data["items"][-1] == vacancy_data


def test_get_vacancies(json_handler):

    json_handler.add_vacancy(
        {"name": "Data Scientist", "link": "http://example.com/job/2", "salary": 7000, "city": "San Francisco"}
    )
    json_handler.add_vacancy(
        {"name": "Software Engineer", "link": "http://example.com/job/1", "salary": 5000, "city": "New York"}
    )

    result = json_handler.get_vacancies(name="Data Scientist")
    assert len(result) == 1
    assert result[0]["name"] == "Data Scientist"


def test_delete_vacancy(json_handler):

    vacancy_data = {
        "name": "Data Scientist",
        "link": "http://example.com/job/2",
        "salary": 7000,
        "city": "San Francisco",
    }
    json_handler.add_vacancy(vacancy_data)

    json_handler.delete_vacancy("Data Scientist")
    assert vacancy_data not in json_handler.data["items"]

    with open(json_handler.filename, "r", encoding="utf-8") as file:
        data = json.load(file)
        assert vacancy_data not in data["items"]
