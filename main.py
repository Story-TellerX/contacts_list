from flask import Flask
from flask import request
from utils import read_txt, gen_users, count_avg_height_weight, count_avg_stat, astronaut_in_space
from api import create_table_users, insert_value_in_table, select_from_table_users, select_from_table_phones, select_from_table_both, delete_from_both

app = Flask("home_work_1")


@app.route('/')
def home_work_1():
    return 'Home Work 1'


@app.route('/requirements/')
def requirements():
    return read_txt()


@app.route('/generate-users/')
def users_name_email():
    query_params = request.args
    count = query_params.get('count') or ''
    default_users_count = 100
    minimum_users_count = 10
    maximum_users_count = 200

    if count.isdigit():
        count = int(count)
        if count > maximum_users_count or count < minimum_users_count:
            count = default_users_count

    else:
        count = default_users_count
    return gen_users(count)


@app.route('/mean/')
def avg_height_weight():
    return count_avg_height_weight()


@app.route('/mean-stat/')
def avg_h_w_stat():
    return count_avg_stat()


@app.route('/space/')
def spaceman_in_space():
    return astronaut_in_space()

# App run - Added a comment to create a difference between the main and homework2 branches
# Added comment to check for updating pull request


@app.route('/create/')
def create_users_table():
    return create_table_users()


@app.route('/select/users/')
def select_from_db_users():
    return select_from_table_users()


@app.route('/select/phones/')
def select_from_db_phones():
    return select_from_table_phones()


@app.route('/select/both/')
def select_from_db():
    return select_from_table_both()


@app.route('/insert/')
def insert_in_db():
    return insert_value_in_table()


@app.route('/delete/')
def delete_from_db():
    return delete_from_both()


if __name__ == '__main__':
    app.run(debug=True)
