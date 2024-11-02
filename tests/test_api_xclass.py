import json
from unittest.mock import Mock, mock_open, patch

import pytest

from src.Class_api import Api_hh
from src.Class_atrub import Class_main
from tests.conftest import api_error


def test_api_error_get():
    with pytest.raises(TypeError, match="не верный ствтус код"):
        Api_hh("Python", 999)


def test_get_api_rest(tmp_path):
    # Мокируем успешный ответ от requests.get
    mock_response_data = {"items": [{"name": "Python Developer"}, {"name": "Data Scientist"}]}
    mock_get = Mock()
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response_data
    with patch("src.Class_api.requests.get", mock_get):
        api_instance = Api_hh("Python", 2)  # Создаем экземпляр класса

        # Подменяем стандартное открытие файла с помощью mock_open
        mocked_open = mock_open()
        with patch("builtins.open", mocked_open):
            api_instance.get_api_rest()  # Выполняем метод, который записывает JSON

            # Проверяем, что файл был записан с корректными данными
            mocked_open.assert_called_once_with("./src/json_vacancy.json", "w", encoding="utf-8")
            handle = mocked_open()
            assert handle.write.call_count == 24
