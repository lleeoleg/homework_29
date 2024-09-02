import psycopg2
from psycopg2 import Error, DatabaseError

try:
    with psycopg2.connect(
        user="postgres",
        password="o14022004",
        host="127.0.0.1",
        port="5432",
        database="postgres_db1",
    ) as connection:
        connection.autocommit = False

        try:
            with connection.cursor() as cursor:
                # cursor.execute("CREATE TABLE homework_table (id SERIAL PRIMARY KEY, column1 VARCHAR(100) NOT NULL, column2 INTEGER, column3 DATE);")
                cursor.execute("SELECT * FROM homework_table;")
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
                print("Чтение строк прошло успешно")
            connection.commit()

        except Exception as error:
            print(f"Ошибка чтения строк: {error}")
            connection.rollback()

except (Exception, Error, DatabaseError) as error:
    print("Ошибка при работе с PostgreSQL", error)

