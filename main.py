from datetime import date, time
from pprint import pprint
from joblib import Memory

from queries import query_free_classrooms, query_classrooms_list
from parsers import parse_classrooms


memory = Memory(cachedir='cache')


@memory.cache
def get_free_classrooms(date, time_from, time_to):
    page = query_free_classrooms(date, time_from, time_to)
    classrooms = parse_classrooms(page)
    return classrooms


@memory.cache
def get_classroom(name_to_query):
    page = query_classrooms_list('eg')
    classrooms = parse_classrooms(page)
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


def save_classrooms_page():
    page = query_classrooms_list('eg')
    with open('classrooms.html', 'wb') as f:
        f.write(page)


def load_classrooms_page():
    with open('classrooms.html', 'rb') as f:
        return f.read()


def test_classrooms():
    classrooms = get_classroom('eg')
    pprint(classrooms)


if __name__ == '__main__':
    # test_free_classrooms()
    # test_classrooms()
    page = load_classrooms_page()
    classrooms = parse_classrooms(page)
    pprint(classrooms)
