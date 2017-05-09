import requests
from bs4 import BeautifulSoup

url = 'https://www7.ceda.polimi.it/spazi/spazi/controller/RicercaAuleLibere.do?\
jaf_currentWFID=main'


def format_line(key, value):
    return 'Content-Disposition: form-data; name="{}"\n\n{}\n'\
            .format(key, value)


params = {
    'spazi___model___formbean___RicercaAvanzataAuleLibereVO___postBack': 'true',
    'spazi___model___formbean___RicercaAvanzataAuleLibereVO___formMode': 'FILTER',
    'spazi___model___formbean___RicercaAvanzataAuleLibereVO___categoriaScelta': 'D',
    'spazi___model___formbean___RicercaAvanzataAuleLibereVO___tipologiaScelta': 'tutte',
    'spazi___model___formbean___RicercaAvanzataAuleLibereVO___sede': 'MIA',
    'spazi___model___formbean___RicercaAvanzataAuleLibereVO___iddipScelto': 'tutti',
    'spazi___model___formbean___RicercaAvanzataAuleLibereVO___sigla': '',
    'spazi___model___formbean___RicercaAvanzataAuleLibereVO___giorno_day': '10',
    'spazi___model___formbean___RicercaAvanzataAuleLibereVO___giorno_month': '5',
    'spazi___model___formbean___RicercaAvanzataAuleLibereVO___giorno_year': '2017',
    'jaf_spazi___model___formbean___RicercaAvanzataAuleLibereVO___giorno_date_format': 'dd/MM/yyyy',
    'spazi___model___formbean___RicercaAvanzataAuleLibereVO___orario_dal': '08:15',
    'spazi___model___formbean___RicercaAvanzataAuleLibereVO___orario_al': '10:15',
    'spazi___model___formbean___RicercaAvanzataAuleLibereVO___soloPreseElettriche_default': 'N',
    'spazi___model___formbean___RicercaAvanzataAuleLibereVO___soloPreseDiRete_default': 'N',
    'evn_ricerca_avanzata': 'Ricerca aule libere'
}

lines = [format_line(key, value)
         for (key, value) in params.items()]

boundary = '----WebKitFormBoundary6baWbSkLbdhksRAi'
separator = '--' + boundary + '\n'

query = separator + separator.join(lines) + '\n' + '--' + boundary + '--'

headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0',
    'Content-Type': 'multipart/form-data; boundary={}'.format(boundary),
    'Content-Length': str(len(query))
})

r = requests.post(url, headers=headers, data=query)

soup = BeautifulSoup(r.text, 'html.parser')

aule = [node.text for node in soup.find_all('b')]
print('\n'.join(aule))
