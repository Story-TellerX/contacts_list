import sqlite3


def create_table_users() -> str:
    # Create connection
    con = sqlite3.connect('./users.db')
    cur = con.cursor()

    # create a sql query
    sql_create_users = """
    CREATE TABLE IF NOT EXISTS users
    (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(25), last_name VARCHAR(50));
    """

    # Create table
    cur.execute(sql_create_users)

    # Save (commit) the changes
    con.commit()

    # Close connection
    con.close()
    return str("table users is created")


def create_table_phones() -> str:
    # Create connection
    con = sqlite3.connect('./users.db')
    cur = con.cursor()

    # create a sql query
    sql_create_phones = """
    CREATE TABLE IF NOT EXISTS phones
    (id INTEGER PRIMARY KEY,
    id_people INTEGER,
    value VARCHAR(20) UNIQUE,
    FOREIGN KEY (id_people)  REFERENCES users (id));
    """

    # Create table
    cur.execute(sql_create_phones)

    # Save (commit) the changes
    con.commit()

    # Close connection
    con.close()
    return str("table phones is created")


def insert_value_in_table() -> str:
    con = sqlite3.connect("./users.db")
    cur = con.cursor()
    sql_insert_value_in_users = """
    INSERT INTO users
    values (null, 'Dima', 'First');
    """
    cur.execute(sql_insert_value_in_users)
    con.commit()
    id_for_phones = int(cur.lastrowid)
    sql_insert_value_in_phones = f"INSERT INTO phones values (null, {id_for_phones}, '+38077111224');"
    cur.execute(sql_insert_value_in_phones)
    con.commit()
    con.close()
    return str("Data in table are update")


def select_from_table_users() -> str:

    con = sqlite3.connect('./users.db')
    cur = con.cursor()

    sql_select_from_users = """
    SELECT * FROM users;
        """

    cur.execute(sql_select_from_users)
    user_list = cur.fetchall()

    # Close connection
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

    # Close connection
    con.close()
    return str(phones_list)


def select_from_table_both() -> str:

    con = sqlite3.connect('./users.db')
    cur = con.cursor()

    sql_select_from_both = """
    SELECT users.id as id, first_name, last_name, value 
    FROM users 
    JOIN phones ON users.id = phones.id;
        """

    cur.execute(sql_select_from_both)
    both_list = cur.fetchall()

    con.close()
    return str(both_list)


def delete_from_both() -> str:

    con = sqlite3.connect('./users.db')
    cur = con.cursor()

    sql_delete_from_users = """
    DELETE FROM  users;
        """
    cur.execute(sql_delete_from_users)
    con.commit()

    sql_delete_from_phones = """
    DELETE FROM  phones;
        """
    cur.execute(sql_delete_from_phones)
    con.commit()

    con.close()

    return f'All data were deleted'
