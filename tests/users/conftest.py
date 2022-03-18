import pytest
import sqlite3
from sqlite3 import Error
from tools import ReadFile

CONFIG_PATH = "tests/users/config.json"


@pytest.fixture(scope='session')
def database():
    data = ReadFile.read_file(CONFIG_PATH)
    try:
        connection = sqlite3.connect(data['name_database'])
        db_session = connection.cursor()
        yield db_session
        db_session.connection.commit()
        db_session.close()
    except Error:
        print(f'Something wrong with sqlite3: {Error}', Error)
