from typing import Dict
from .database_connector import DatabaseConnection
from .interfaces.database_repository import DatabaseRepositoryInterface


class DatabaseRepository(DatabaseRepositoryInterface):
    @classmethod
    def insert_artist(cls, data: Dict) -> None:
        query = """
                INSERT INTO artists
                    (first_name, second_name, nickname, artist_id, link, extraction_date)
                VALUES
                (%s, %s, %s, %s, %s, %s,)
                """

        cursor = DatabaseConnection.connection.cursor()
        cursor.execute(query, list(data.values()))
        DatabaseConnection.connection.commit()
