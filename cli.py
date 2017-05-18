#!/usr/bin/env python3
from pprint import pprint

import click
from click_datetime import Datetime

from polimi import get_classroom_list, get_free_classrooms


@click.group()
def cli():
    pass


@cli.group('classrooms')
def classrooms():
    pass


@classrooms.command('search')
@click.argument('name')
def classrooms_search(name):
    result = get_classroom_list(name)
    pprint(result)


@classrooms.command('free')
@click.argument('day', type=Datetime(format='%d/%m/%Y'))
@click.argument('time_from', type=Datetime(format='%H:%M'))
@click.argument('time_to', type=Datetime(format='%H:%M'))
def classrooms_free(day, time_from, time_to):
    response = get_free_classrooms(day, time_from, time_to)
    pprint(response)


if __name__ == '__main__':
    cli()
