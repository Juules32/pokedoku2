import code, psycopg2, os, json
from typing import Any, Union
from dotenv import load_dotenv
from enum import Enum

class Fetch(Enum):
    ONE = 0
    ALL = 1

class Database:
    def __init__(self, connection_string):

        self.connection_string = connection_string
        try:
            self.connection = psycopg2.connect(self.connection_string)
            print("Connection to the database established successfully")
        except Exception as e:
            print(f"Error: {e}")    

    def commit_query(self, query: str, vars: Any = None, fetch: Union[Fetch, None] = None, message: Union[str, None] = None) -> Any:
        try:
            with self.connection.cursor() as cur:
                cur.execute(query=query, vars=vars)
                result = None
                if fetch:
                    match fetch:
                        case Fetch.ONE:
                            result = cur.fetchone()
                            if result:
                                result = result[0]
                        case Fetch.ALL:
                            result = cur.fetchall()
                self.connection.commit()
                if message:
                    print(message)
                return result
        except Exception as e:
            print(f"Error: {e}")
            self.connection.rollback()

    def create_puzzle_table(self):
        self.drop_table(table_name="puzzle")

        query = """
            CREATE TABLE puzzle (
                date DATE PRIMARY KEY,
                data JSON NOT NULL
            );
        """
        self.commit_query(query=query, message="Created puzzle table successfully")

    def drop_table(self, table_name: str) -> None:
        query = f"""
            DROP TABLE IF EXISTS {table_name};
        """
        self.commit_query(
            query=query, 
            message=f"Dropped {table_name} table successfully (if it existed)"
        )

    def set_puzzle(self, date: str, data: dict) -> None:
        # Insert date and data, overwriting old data if it already exists
        query = """
            INSERT INTO puzzle (date, data)
            VALUES (%s, %s)
            ON CONFLICT (date) DO UPDATE SET data = EXCLUDED.data;
        """
        data_string: str = json.dumps(data)
        self.commit_query(
            query=query, 
            vars=(date, data_string), 
            message=f"Inserted puzzle data for date: {date} successfully"
        )

    def get_puzzle(self, date: str) -> dict:
        query = """
            SELECT data FROM puzzle WHERE date = %s
        """
        data: dict = self.commit_query(
            query=query, 
            vars=(date,), 
            fetch=Fetch.ONE, 
            message=f"Got data for date: {date} successfully"
        )
        return data

load_dotenv()

connection_string = os.getenv("CONNECTION_STRING")

db = Database(connection_string)

# Running this script sets up the database tables
if __name__ == "__main__":
    db.create_puzzle_table()

    # code.interact(local=locals())
