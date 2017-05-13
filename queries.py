import requests


def query_free_classrooms(day, month, year, time_from, time_to):
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


def query_classrooms_list(name_to_query):
    url = 'https://www7.ceda.polimi.it/spazi/spazi/controller/RicercaAula.do'

    key_head = 'spazi___model___formbean___RicercaAvanzataAuleVO___'

    params = {
        'postBack': 'true',
        'formMode': 'FILTER',
        'sede': 'tutte',
        'sigla': name_to_query,
        'categoriaScelta': 'tutte',
        'tipologiaScelta': 'tutte',
        'iddipScelto': 'tutti',
        'soloPreseElettriche_default': 'N',
        'soloPreseDiRete_default': 'N',
    }

    # prepend key_head to each param
    params = {key_head + key: value
              for key, value in params.items()}

    params['evn_ricerca_avanzata'] = 'Ricerca+aula'
    params['default_event'] = 'evn_ricerca_aula_semplice'

    headers = requests.utils.default_headers()
    headers.update({
        'User-Agent': 'Mozilla/5.0',
    })

    r = requests.get(url, headers=headers, params=params)

    return r.text
