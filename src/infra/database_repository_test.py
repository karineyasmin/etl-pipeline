import pytest
from src.stages.contracts.mocks.transform_contract import transform_contract_mock
from src.infra.database_connector import DatabaseConnection
from src.infra.database_repository import DatabaseRepository


@pytest.mark.skip(reason="No need to insert data into database")
def test_insert_artist():
    DatabaseConnection.connect()

    database_repo = DatabaseRepository()
    data = transform_contract_mock.load_content[0]
    database_repo.insert_artist(data)
