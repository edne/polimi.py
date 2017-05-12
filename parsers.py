from bs4 import BeautifulSoup


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
