from bs4 import BeautifulSoup
import re


def parse_col(col):
    text = col.text
    text = text.split()
    text = ' '.join(text)
    return text


def parse_classroom_id(row):
    a, = row.find_all('a')
    href = a['href']
    return re.search('(?<=idaula=)\d+', href).group(0)


def parse_classroom_info(row):
    cols = row.find_all('td')

    classroom_id = parse_classroom_id(row)

    parsed = [parse_col(col) for col in cols]
    where, name, details, category, type_, department = parsed

    return {'where': where,
            'name': name,
            'id': classroom_id,
            'category': category,
            'type': type_,
            'department': department}


def parse_classroom_list(page):
    soup = BeautifulSoup(page, 'html.parser')
    rows = soup.find_all('tr')

    classrooms = [parse_classroom_info(row)
                  for row in rows
                  if len(row.find_all('td')) == 6]
    return classrooms


def parse_info(row):
    italics = row.find_all('i')
    if italics:
        info_name = italics[0].text

        info = row.text
        info = info.replace(info_name, '')
        info = info.split()
        info = ' '.join(info)
        return info_name, info
    else:
        return None


def parse_classroom(page):
    soup = BeautifulSoup(page, 'html.parser')
    rows = soup.find_all('td', class_='ElementInfoCard1')

    infos = [parse_info(r) for r in rows]
    infos = [i for i in infos if i]  # filter away None
    infos = dict(infos)
    return infos
