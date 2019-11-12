import sqlite3


def main():
    connection = sqlite3.connect('crm.db')

    sql = """create table users (
             name text,
             age integer
    )"""

    cursor = connection.cursor()

    cursor.execute(sql)

    connection.commit()

    connection.close()


if __name__ == '__main__':
    main()
