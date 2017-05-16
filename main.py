from datetime import date, time
from pprint import pprint
from joblib import Memory

from queries import query_free_classrooms, query_classrooms_list
from parsers import parse_classroom_list, parse_classroom


memory = Memory(cachedir='cache')


@memory.cache
def get_free_classrooms(date, time_from, time_to):
    page = query_free_classrooms(date, time_from, time_to)
    classrooms = parse_classroom_list(page)
    return classrooms


@memory.cache
def get_classroom_list(name_to_query):
    page = query_classrooms_list('eg')
    classrooms = parse_classroom_list(page)
    return classrooms


def test_free_classrooms():
    day = date(2017, 5, 15)
    time_from = time(10, 15)
    time_to = time(11, 15)

    classrooms = get_free_classrooms(day, time_from, time_to)
    if not classrooms:
        # TODO: handle invalid server response
        get_free_classrooms.clear()

    pprint(classrooms)


def save_classroom_list():
    page = query_classrooms_list('eg')
    with open('classroom_list.html', 'wb') as f:
        f.write(page)


def load_classroom_list():
    with open('classroom_list.html', 'rb') as f:
        return f.read()


def load_classroom():
    with open('classroom.html', 'rb') as f:
        return f.read()


def test_classroom_list():
    classrooms = get_classroom_list('eg')
    pprint(classrooms)


if __name__ == '__main__':
    # test_free_classrooms()
    # test_classrooms()
    page = load_classroom()
    classrooms = parse_classroom(page)
    pprint(classrooms)
