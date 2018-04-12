# Bot Template

Es la base para crear bots de telegram.

## Requerimientos

- Python 3.5+
- PipEnv [https://docs.pipenv.org/](https://docs.pipenv.org/)


## (Mac) Instalación con Homebrew

Se utilizarán los comandos de mac con homebrew [https://brew.sh/](https://brew.sh/)


```bash

$ brew install python && brew install pipenv

```

## (Unix) Instalacion con Pipsi

- Pipsi  [https://github.com/mitsuhiko/pipsi](https://github.com/mitsuhiko/pipsi)
- Pew [https://github.com/berdario/pew](https://github.com/berdario/pew)

### Instalar Pipsi

```bash

$ curl https://raw.githubusercontent.com/mitsuhiko/pipsi/master/get-pipsi.py | python3 - --src 'git+https://github.com/mitsuhiko/pipsi.git#egg=pipsi'

```

Agregar la ruta de *pipsi* al PATH en `.bashrc` o `.zshrc`


```bash
  
  export PATH=/home/<user>/.local/bin:$PATH

```

Instalar *pipenv* y *pew*

```bash

$ pipsi install pipenv
$ pipsi install pew

```

## Ejecución

Se debe ejecutar el comando

```bash

$ pipenv install && pipenv shell

```

Para poder instalar las dependencias y habilitar el entorno.

Luego se debe configuar el archivo `.env`

```bash

$ cp env.example .env
$ vim .env

```

Finalmente ejecutar el bot con

```bash

$ python .

```


## Paquetes Recomendados

Los siguientes paquetes pueden ser de utilidad para crear un bot.
También se recomienda seguir patrones de diseño como:

- PyPattyrn [https://github.com/tylerlaberge/PyPattyrn](https://github.com/tylerlaberge/PyPattyrn)
- Facades [https://github.com/faif/python-patterns](https://github.com/faif/python-patterns)

### Crypto

- PyChaucha [https://github.com/proyecto-chaucha/pychaucha](https://github.com/proyecto-chaucha/pychaucha)
- CryptoDome (https://www.pycryptodome.org)
- Passlib (https://passlib.readthedocs.io/en/stable/)
- Bit [https://github.com/ofek/bit](https://github.com/ofek/bit)

### Telegram

- Python Telegram Bot (https://python-telegram-bot.readthedocs.io)
- Emoji (https://github.com/carpedm20/emoji)

### Comunicación

- Requests (http://docs.python-requests.org/)
- ParsePy (https://github.com/milesrichardson/ParsePy)
- Socket.io (http://python-socketio.readthedocs.io)
- Json API Requests (https://github.com/socialwifi/jsonapi-requests)
- Python JWT (https://github.com/davedoesdev/python-jwt)

### Utilidades

- Jinja2 (http://jinja.pocoo.org/)
- Babel (http://babel.pocoo.org)
- Money (https://github.com/vimeo/py-money)
- Flufli18n (https://flufli18n.readthedocs.io)
- Arrow (https://arrow.readthedocs.io/en/latest/)
- Crython (https://github.com/ahawker/crython)
- Promises (https://github.com/syrusakbary/promise)
- Events (http://events.readthedocs.io/en/latest/)
- PyFileSystem (https://www.pyfilesystem.org/)
- Unipath (https://github.com/mikeorr/Unipath)
- Natural Language (http://www.nltk.org/)
- PyOTP - 2 Factor Auth (https://github.com/pyotp/pyotp)

### Almacenamiento y Validación

- Redis (https://pypi.python.org/pypi/redis)
- PonyOrm (https://ponyorm.com/)
- Pewee (https://github.com/coleifer/peewee)
- Blitz (http://blitzdb.readthedocs.io/en/latest/)
- Cerberus (http://docs.python-cerberus.org/)
- DiskCache (http://www.grantjenks.com/docs/diskcache/)

### Configuración

- EnvParse (https://github.com/rconradharris/envparse)
- JsonLogger (https://github.com/madzak/python-json-logger)
- SimpleJson (https://simplejson.readthedocs.io/en/latest/)
- HJson (https://github.com/hjson/hjson-py)


### Herramientas para Pruebas

- The (http://the-py.github.io/the/)
- Green (https://github.com/CleanCut/green)
- Flake8 (http://flake8.pycqa.org)
- FactoryBoy (https://github.com/FactoryBoy/factory_boy)
