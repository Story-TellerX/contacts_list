import csv
import statistics
import requests

from faker import Faker


def read_txt() -> str:
    # Сорри забыл переписать на with as - написал первый вариант кода и забыл поправить (
    with open("requirements.txt", "r") as open_file:
        read_file = open_file.read()
    return read_file


def gen_users(count: int = 100) -> str:
    faker = Faker()
    name_email = []
    for i in range(count):
        gen_name = f'{faker.name()} {faker.email()}'
        name_email.append(gen_name)
    return str(name_email)  # Поправил тип данных


#  Оставил первое решение через csv риадер, так как на нем разобрался как
#  работает данный модуль

# def count_avg_height_weight():
#     with open('hw_1.csv') as open_csv_file:
#         source = csv.reader(open_csv_file, delimiter=",", skipinitialspace=True, doublequote=True)
#         next(source)  # skipping header
#         only_heights_f = []
#         only_weights_f = []
#         all_data = list(source)
#         del all_data[-1]  # del empty value
#         only_heights = [i[-2] for i in all_data]
#         for item in only_heights:
#             only_heights_f.append(float(item) * 2.54)
#         only_heights_len = len(only_heights)
#         only_weights = [i[-1] for i in all_data]
#         for item in only_weights:
#             only_weights_f.append(float(item) * 0.45359237)
#         only_weights_len = len(only_weights)
#         the_sum_h = 0
#         for i in only_heights_f:
#             the_sum_h = the_sum_h + i
#         the_sum_w = 0
#         for i in only_weights_f:
#             the_sum_w = the_sum_w + i
#         avg_heights = the_sum_h / only_heights_len
#         avg_weights = the_sum_w / only_weights_len
#         answer = f"Средний орост составляет: {avg_heights} см, а средний вес соствляет: {avg_weights} кг."
#     return answer


#  Вспомагательные функции с переводом значения в float, а потом в метрическую систему измерений
def result_to_sm(item):
    result_sm = float(item)*2.54
    return result_sm


def result_to_kg(item):
    result_kg = float(item)*0.45359237
    return result_kg


def count_avg_height_weight() -> str:
    heights_list = []
    weights_list = []
    with open("hw_1.csv", "r") as csv_file:
        reader_csv_file = csv.DictReader(csv_file, delimiter=",", skipinitialspace=True, doublequote=True)
        for row in reader_csv_file:
            heights = row["Height(Inches)"]
            weights = row["Weight(Pounds)"]
            if heights is not None and heights != 0:
                heights_list.append(result_to_sm(heights))
            if weights is not None and weights != 0:
                weights_list.append(result_to_kg(weights))
                #  получаем значения строки столбца с использованием хедера приводим к float
                #  и переводим значеие в метрическую систему измерений
                #  после чего добавлям значение в список
    avg_heights = sum(heights_list) / len(heights_list)
    avg_heights_stat = statistics.mean(heights_list)
    avg_weights = sum(weights_list) / len(weights_list)
    avg_weights_stat = statistics.mean(weights_list)
    answer = f"avg of heights: {avg_heights} sm, avg of weights: {avg_weights} kg, и модуль статистики говорит, что не так все просто с числами в списке - средний рост: {avg_heights_stat} см и средний вес: {avg_weights_stat} кг"
    return answer


#  Второе решение данной задачи через модуль статистики и построчное считываение


def count_avg_stat() -> str:
    with open('hw_1.csv') as csv_files:
        source = csv.reader(csv_files, delimiter=",", skipinitialspace=True, doublequote=True)
        next(source)  # skipping header
        only_heights_f = []
        only_weights_f = []
        all_data = list(source)
        del all_data[-1]  # del empty value
        only_heights = [i[-2] for i in all_data]
        for item in only_heights:
            only_heights_f.append(float(item) * 2.54)
        only_weights = [i[-1] for i in all_data]
        for item in only_weights:
            only_weights_f.append(float(item) * 0.45359237)
        avg_heights = statistics.mean(only_heights_f)
        avg_weights = statistics.mean(only_weights_f)
        answer = f"Средний орост составляет: {avg_heights} см, а средний вес соствляет: {avg_weights} кг."
    return answer


def astronaut_in_space() -> str:
    r = requests.get('http://api.open-notify.org/astros.json')
    all_data = r.json()
    numbers = all_data["number"]
    names = all_data["people"]
    names_astro = []
    for d in names:
        names_astro.append(d['name'])
    answer = f"\n Всего в космосе: {numbers} космонавтов. \n\n\n Вот имена этих смельчаков: \n {names_astro}"
    return answer
