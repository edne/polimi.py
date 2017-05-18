from datetime import date, time
from pprint import pprint
from polimi import get_free_classrooms, query_classrooms_list,\
                   get_classroom_list, get_classroom


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
    with open('test_data/classroom_list.html', 'wb') as f:
        f.write(page)


def load_classroom_list():
    with open('test_data/classroom_list.html', 'rb') as f:
        return f.read()


def load_classroom():
    with open('test_data/classroom.html', 'rb') as f:
        return f.read()


def test_classroom_list():
    classrooms = get_classroom_list('eg')
    pprint(classrooms)


if __name__ == '__main__':
    # test_free_classrooms()
    # test_classrooms()

    # page = load_classroom()
    # info = parse_classroom(page)
    info = get_classroom(20)
    pprint(info)
