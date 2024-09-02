import psycopg2
from psycopg2 import Error, DatabaseError

def read_one_row(connection, row_id):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM homework_table WHERE id = %s;", (row_id,))
            row = cursor.fetchone()
            if row:
                print(f"Строка с ID {row_id}: {row}")
            else:
                print(f"Строка с ID {row_id} не найдена.")
    except Exception as error:
        print(f"Ошибка чтения строки: {error}")

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
            read_one_row(connection, 1)

            connection.commit()

        except Exception as error:
            print(f"Ошибка выполнения операций: {error}")
            connection.rollback()

except (Exception, Error, DatabaseError) as error:
    print("Ошибка при работе с PostgreSQL", error)
