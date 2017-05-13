from datetime import date, time
from pprint import pprint
from joblib import Memory

from queries import query_free_classrooms, query_classrooms_list
from parsers import parse_classrooms_list_page


memory = Memory(cachedir='cache')


@memory.cache
def get_free_classrooms(day, time_from, time_to):
    page = query_free_classrooms(str(day.day),
                                 str(day.month),
                                 str(day.year),
                                 time_from.strftime('%H:%M'),
                                 time_to.strftime('%H:%M'))
    classrooms = parse_classrooms_list_page(page)
    return classrooms


@memory.cache
def get_classroom_list(name_to_query):
    page = query_classrooms_list('eg')
    classrooms = parse_classrooms_list_page(page)
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


if __name__ == '__main__':
    # test_free_classrooms()
    classrooms = get_classroom_list('eg')
    pprint(classrooms)
