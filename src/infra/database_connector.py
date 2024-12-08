import mysql.connector as mysql
import os
from dotenv import load_dotenv


class DatabaseConnection:
    connection = None

    @classmethod
    def connect(cls):
        load_dotenv()
        db_connection = mysql.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database="pipeline_db",
            user=os.getenv("DB_USER"),
            passwd=os.getenv("DB_PASSWORD"),
        )
        cls.connection = db_connection
