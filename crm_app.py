import sqlite3


def main():
    print('===== Welcome to CRM Application ====='
          '\n[S]how: Show all users info'
          '\n[A]dd: Add new user'
          '\n[F]ind: Find user'
          '\n[D]elete: Delete user'
          '\n[E]dit: Edit user info'
          '\n======================================')
    while True:
        select_menu = input()

        if select_menu == 'A' or select_menu == 'a':
            print(f'Your command > {select_menu}')
            new_name = input('New user name > ')
            new_age = input('New user age > ')

            print(f'Duplicated user name {new_name}')

        if len(new_name) < 1:
            print(f"User name can't be blank")

        elif len(new_name) > 20:
            print(f"User name is too long(maximum is 20 characters)")

        elif new_age == '':
            print(f"age can't be blank")

        else:
            if check_int(new_age) == False:
                print(f"Age is not positive integer")
            else:
                try:
                    register_user(new_name, new_age)
                    print(f'Add new user: {new_name}')

                except sqlite3.IntegrityError:
                    print(f'Duplicated user name {new_name}')





        elif select_menu == 'S' or select_menu == 's':
            print(f'Your command > {select_menu}')
            users = show_users()

            for user in users:
                print(f'Name: {user[0]}, Age: {user[1]}')

        elif select_menu == 'F' or select_menu == 'f':
            print(f'Your command > {select_menu}')
            find_name = input('User name > ')

            try:
                print(f'Name: {find_user(find_name)[0]} Age: {find_user(find_name)[1]}')
            except TypeError:
                print(f'Sorry, {find_name} is not found')

        elif select_menu == 'D' or select_menu == 'd':
            print(f'Your command > {select_menu}')
            delete_name = input('User name > ')

            delete_user(delete_name)
            print(f'{delete_name} is deleted')

        elif select_menu == 'E' or select_menu == 'e':

            pre_edit_name = input('User name > ')

            try:
                edit_name = input(f'New user name ({find_user(pre_edit_name)[0]})  > ')
                edit_age = input(f'New user age ({find_user(pre_edit_name)[1]})  > ')
                edit_user_name(pre_edit_name, edit_name, edit_age)
            except TypeError:
                print(f'Sorry, {pre_edit_name} is not found')

        elif select_menu == 'Q' or select_menu == 'q':
            print(f'Your command > {select_menu}')
            print(f'Bye!')
            break


        else:
            print(f'Your command > {select_menu}')
            print(f'{select_menu}: command not found')


def register_user(name, age):
    connection = sqlite3.connect('crm.db')
    cursor = connection.cursor()
    sql = f"INSERT INTO users (name,age) VALUES(?,?)"
    cursor.execute(sql, (name, age))
    connection.commit()
    connection.close()


def show_users():
    connection = sqlite3.connect('crm.db')
    cursor = connection.cursor()
    sql = f"SELECT * FROM users"
    users = cursor.execute(sql).fetchall()
    connection.close()
    return users


def delete_user(delete_name):
    connection = sqlite3.connect('crm.db')
    cursor = connection.cursor()
    sql = f"DELETE FROM users  WHERE name = ?"
    cursor.execute(sql, (delete_name,))
    connection.commit()
    connection.close()


def find_user(find_name):
    connection = sqlite3.connect('crm.db')
    cursor = connection.cursor()
    sql = f"SELECT * FROM users  WHERE name == '{find_name}'"
    find_user = cursor.execute(sql).fetchone()
    connection.close()
    return find_user


def edit_user_name(pre_edit_name, edit_name, edit_age):
    connection = sqlite3.connect('crm.db')
    cursor = connection.cursor()
    sql = f"UPDATE users SET name = '{edit_name}',age = '{edit_age}'  WHERE name = '{pre_edit_name}'"
    cursor.execute(sql)
    connection.commit()
    connection.close()


def check_int(age):
    try:
        int(age)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    main()
