from joblib import Memory
from queries import query_free_classrooms, query_classrooms_list,\
                    query_classroom
from parsers import parse_classroom_list, parse_classroom


memory = Memory(cachedir='cache')


@memory.cache
def get_free_classrooms(date, time_from, time_to):
    page = query_free_classrooms(date, time_from, time_to)
    classrooms = parse_classroom_list(page)
    return classrooms


@memory.cache
def get_classroom_list(name_to_query):
    page = query_classrooms_list(name_to_query)
    classrooms = parse_classroom_list(page)
    return classrooms


@memory.cache
def get_classroom(classroom_id):
    page = query_classroom(classroom_id)
    info = parse_classroom(page)
    return info
