# polimi.py

Unofficial Python library to access public available informations from
[Politecnico di Milano](http://www.polimi.it/) website.

**Work in progress**, for now it only takes informations about classrooms and
their occupation.


## Usage

```
pip install -r requirements.txt
```

### From the command line interface
```
./cli.py classrooms free 25/05/2017 17:00 18:00
```

```
./cli.py classrooms search "E.G.1"
```

It works also with partial queries, like `eg` or `d.0`.

Output example:
```
[{'category': 'AULA DIDATTICA',
  'department': '-',
  'id': '19',
  'name': 'E.G.1',
  'type': 'PLATEA FRONTALE',
  'where': 'Milano Città Studi, Via Bassini'}]
```

### As library
Read the [source](polimi/__init__.py).


## Contributing

Contributions are welocome, please follow the
[PEP8](https://www.python.org/dev/peps/pep-0008/) standard if you wanto to write
code.

If you need a feature feel free to open an issue.


## Acknowledgements and license

Based on the work of @TopoDiFogna in his [Telegram bot](https://github.com/TopoDiFogna/poli_telegram_bot).


Released under the terms of [GNU Affero General Public
License](https://www.gnu.org/licenses/agpl-3.0.en.html).
**TL; DR:** if you modify this library and use it to make "cloud" services you
have to release the modified code.
