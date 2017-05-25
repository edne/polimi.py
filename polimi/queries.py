import requests


def make_headers():
    headers = requests.utils.default_headers()
    headers.update({
        'User-Agent': 'Mozilla/5.0',
    })
    return headers


def prepend_params(params, action):
    key_head = 'spazi___model___formbean___{}VO___'.format(action)

    # prepend key_head to each param
    params = {key_head + key: value
              for key, value in params.items()}

    return params


def make_post_payload(params, boundary):
    def format_line(key, value):
        return 'Content-Disposition: form-data; name="{}"\n\n{}\n'\
                .format(key, value)

    lines = [format_line(key, value)
             for (key, value) in params.items()]

    separator = '--' + boundary + '\n'
    payload = separator + separator.join(lines) + '\n' + '--' + boundary + '--'
    return payload


def query_free_classrooms(date, time_from, time_to):
    day = str(date.day)
    month = str(date.month)
    year = str(date.year)

    time_from = time_from.strftime('%H:%M')
    time_to = time_to.strftime('%H:%M')

    url = 'https://www7.ceda.polimi.it/spazi/spazi/controller/'\
          'RicercaAuleLibere.do'

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
    params = prepend_params(params, 'RicercaAvanzataAuleLibere')

    params['evn_ricerca_avanzata'] = 'Ricerca aule libere'

    boundary = '--lol'
    payload = make_post_payload(params, boundary)

    headers = make_headers()
    headers.update({
        'Content-Type': 'multipart/form-data; boundary=' + boundary,
    })

    r = requests.post(url, headers=headers, data=payload)
    return r.text


def query_classrooms_list(name_to_query):
    url = 'https://www7.ceda.polimi.it/spazi/spazi/controller/RicercaAula.do'

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
    params = prepend_params(params, 'RicercaAvanzataAule')

    params['evn_ricerca_avanzata'] = 'Ricerca+aula'
    params['default_event'] = 'evn_ricerca_aula_semplice'

    r = requests.get(url, headers=make_headers(), params=params)
    return r.text


def query_classroom(classroom_id):
    url = 'https://www7.ceda.polimi.it/spazi/spazi/controller/Aula.do'
    params = {
        'idaula': classroom_id
    }
    r = requests.get(url, headers=make_headers(), params=params)
    return r.text
