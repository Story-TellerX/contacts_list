import sqlite3


def create_table_users():
    # Create connection
    con = sqlite3.connect('./users.db')
    cur = con.cursor()

    # create a sql query
    sql_create_users = """
    CREATE TABLE IF NOT EXISTS users
    (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(25), last_name VARCHAR(50))
    """

    # Create table
    cur.execute(sql_create_users)

    # Save (commit) the changes
    con.commit()

    # Close connection
    con.close()
    return str("table users is created")


def create_table_phones():
    # Create connection
    con = sqlite3.connect('./users.db')
    cur = con.cursor()

    # create a sql query
    sql_create_phones = """
    CREATE TABLE IF NOT EXISTS phones
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    value VARCHAR(20) UNIQUE,
    FOREIGN KEY (id)  REFERENCES users (id))
    """

    # Create table
    cur.execute(sql_create_phones)

    # Save (commit) the changes
    con.commit()

    # Close connection
    con.close()
    return str("table phones is created")
