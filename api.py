import sqlite3


def create_table_users() -> str:
    # Create connection
    con = sqlite3.connect('./users.db')
    cur = con.cursor()

    # create a sql query
    sql_create_users = """
    CREATE TABLE IF NOT EXISTS users
    (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(25) UNIQUE);
    """
    # Create table
    cur.execute(sql_create_users)

    sql_create_phones = """
    CREATE TABLE IF NOT EXISTS phones
    (id INTEGER PRIMARY KEY,
    id_people INTEGER,
    value VARCHAR(20),
    FOREIGN KEY (id_people)  REFERENCES users (id) ON DELETE CASCADE);
    """
    # It should be create an ability to delete data from user and data from phones will be deleted by cascade
    # Create table
    cur.execute(sql_create_phones)

    # Save (commit) the changes
    con.commit()

    # Close connection
    con.close()
    return str("tables users and phones are created")


def insert_value_in_table(name: str, phone: str) -> str:
    con = sqlite3.connect("./users.db")
    cur = con.cursor()

    sql_insert_value_in_users = f"INSERT INTO users values (null,'{name}');"
    cur.execute(sql_insert_value_in_users)

    sql_insert_value_in_phones = f"INSERT INTO phones values (null, (SELECT id FROM users WHERE name='{name}'), '{phone}');"
    cur.execute(sql_insert_value_in_phones)
    # Added relates for user name and phone number
    con.commit()
    con.close()
    return str("Data in table are updated")


def select_from_table_users() -> str:

    con = sqlite3.connect('./users.db')
    cur = con.cursor()

    sql_select_from_users = """
    SELECT * FROM users;
    """

    cur.execute(sql_select_from_users)
    user_list = cur.fetchall()

    con.close()
    return str(user_list)


def select_from_table_phones() -> str:

    con = sqlite3.connect('./users.db')
    cur = con.cursor()

    sql_select_from_phones = """
    SELECT * FROM phones;
    """

    cur.execute(sql_select_from_phones)
    phones_list = cur.fetchall()

    con.close()
    return str(phones_list)


def select_from_table_both() -> str:

    con = sqlite3.connect('./users.db')
    cur = con.cursor()

    sql_select_from_both = """
    SELECT users.id as id, name, value 
    FROM users 
    JOIN phones ON users.id = phones.id_people;
    """
    # Create SELECT JOIN for user with select phones that they have
    cur.execute(sql_select_from_both)
    both_list = cur.fetchall()

    con.close()
    return str(both_list)


def delete_from_both() -> str:

    con = sqlite3.connect('./users.db')
    cur = con.cursor()

    sql_delete_from_users = """
    DELETE FROM users;
    """
    cur.execute(sql_delete_from_users)

    sql_delete_from_phones = """
    DELETE FROM phones;
    """
    cur.execute(sql_delete_from_phones)
    con.commit()

    con.close()

    return str("All data were deleted")


def delete_from_db_by_id(name: str) -> str:
    con = sqlite3.connect('./users.db')
    cur = con.cursor()

    sql_delete_from_users = f"DELETE FROM users WHERE name='{name}';"
    sql_delete_from_phones = f"DELETE FROM phones WHERE id=(SELECT id FROM users WHERE name='{name}')"
    # Deleting data from phones when some user was selected for deleting and delete record about user

    cur.execute(sql_delete_from_phones)
    cur.execute(sql_delete_from_users)

    con.commit()

    con.close()
    return str(f'User with name {name} was deleted')
