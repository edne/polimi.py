from datetime import date, time
from pprint import pprint
from bs4 import BeautifulSoup
from joblib import Memory

from queries import query_free_classrooms


def get_cols(row):
    return row.find_all('td')


def parse_col(col):
    text = col.text
    text = text.split()
    text = ' '.join(text)
    return text


def get_classroom(row):
    cols = get_cols(row)
    parsed = [parse_col(col) for col in cols]
    where, name, details, category, type_, department = parsed
    return {'where': where,
            'name': name,
            'category': category,
            'type': type_,
            'department': department}


def parse_classrooms_list_page(page):
    soup = BeautifulSoup(page, 'html.parser')
    rows = soup.find_all('tr')

    classrooms = [get_classroom(row)
                  for row in rows
                  if len(get_cols(row)) == 6]
    return classrooms


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


day = date(2017, 5, 15)
time_from = time(10, 15)
time_to = time(11, 15)

classrooms = get_free_classrooms(day, time_from, time_to)
if not classrooms:
    # TODO: handle invalid server response
    get_free_classrooms.clear()


pprint(classrooms)
