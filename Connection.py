import pytest
import pyodbc

@pytest.fixture(scope="session")
def db_connection():
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=JAYARAM\\DEVELOPER1;"
        "DATABASE=test2;"
        "UID=JaiLogin;"
        "PWD=Jayaram@300"
    )
    yield conn
    conn.close()


def test_addition(db_connection):
    a, b = 2, 3
    result = a + b
    cursor = db_connection.cursor()
    cursor.execute(
        "INSERT INTO test2.dbo.Details (Name, Id, Class) VALUES (?, ?, ?)",
        ('H', 8, 78)
    )
    cursor.execute(
        "INSERT INTO test2.dbo.Details (Name, Id, Class) VALUES (?, ?, ?)",
        ('I', 9, 100)
    )
    db_connection.commit()
    assert result == 5
