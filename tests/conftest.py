import pytest

from src.Class_api import Api_hh


@pytest.fixture
def api_error():
    return Api_hh("Python", 999)
