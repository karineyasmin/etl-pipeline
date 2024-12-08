from .database_connector import DatabaseConnection


def test_connect():
    print()
    print(DatabaseConnection.connection)
    assert DatabaseConnection.connection is None
    DatabaseConnection.connect()
    print()
    print(DatabaseConnection.connection)
    assert DatabaseConnection.connection is not None
