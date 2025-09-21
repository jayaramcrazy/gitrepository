from logging import exception

import pyodbc
import pytest


@pytest.fixture(scope="session")
def connection():
    conn = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=JAYARAM\\DEVELOPER1;"
            "DATABASE=test3;"
            "UID=JaiLogin;"
            "PWD=Jayaram@300"
    )

    yield conn
    conn.close()


def test_addition(connection):
    a , b = 2,4
    result = a + b
    try:
        cursor = connection.cursor()
        connection.commit()
        cursor.execute(
            "INSERT INTO test3.dbo.Studentdetails(studentRno , name , marks) VALUES(?, ?, ?);",
            (9,'lio',34))

        cursor.execute("SELECT TOP 1 * FROM test3.dbo.Studentdetails ORDER BY studentRno DESC")
        row = cursor.fetchone()
        print("Last inserted row:", row)
        assert result == 6

    except exception as e:
        print('Some Error',e)

    else:
        print('Inserting is done')