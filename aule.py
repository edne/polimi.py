import requests
from bs4 import BeautifulSoup

day = '10'
month = '5'
year = '2017'
time_from = '10:15'
time_to = '11:15'


def get_page():
    url = 'https://www7.ceda.polimi.it/spazi/spazi/controller/'\
          'RicercaAuleLibere.do?jaf_currentWFID=main'

    key_head = 'spazi___model___formbean___RicercaAvanzataAuleLibereVO___'

    params = {
        'postBack': 'true',
        'formMode': 'FILTER',
        'categoriaScelta': 'D',
        'tipologiaScelta': 'tutte',
        'sede': 'MIA',
        'iddipScelto': 'tutti',
        'sigla': '',
        'giorno_day': day,
        'giorno_month': month,
        'giorno_year': year,
        'orario_dal': time_from,
        'orario_al': time_to,
        'soloPreseElettriche_default': 'N',
        'soloPreseDiRete_default': 'N',
        'giorno_date_format': 'dd/MM/yyyy',
    }

    # prepend key_head to each param
    params = {key_head + key: value
              for key, value in params.items()}

    params['evn_ricerca_avanzata'] = 'Ricerca aule libere'

    def format_line(key, value):
        return 'Content-Disposition: form-data; name="{}"\n\n{}\n'\
                .format(key, value)

    lines = [format_line(key, value)
             for (key, value) in params.items()]

    boundary = '----WebKitFormBoundary6baWbSkLbdhksRAi'
    separator = '--' + boundary + '\n'

    payload = separator + separator.join(lines) + '\n' + '--' + boundary + '--'

    headers = requests.utils.default_headers()
    headers.update({
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'multipart/form-data; boundary={}'.format(boundary),
        'Content-Length': str(len(payload))
    })

    r = requests.post(url, headers=headers, data=payload)

    return r.text


def get_page_from_file(file_name):
    with open(file_name) as f:
        page = f.read()
    return page


def save_page(file_name, page):
    with open(file_name, "w") as f:
        f.write(page)


# page = get_page()
# save_page('page.html', page)

page = get_page_from_file('page.html')

soup = BeautifulSoup(page, 'html.parser')

aule = [node.text for node in soup.find_all('b')]
print('\n'.join(aule))
