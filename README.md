# Bot Template

Es la base para crear bots de telegram.

## Requerimientos

- Python 3.5+
- PipEnv [https://docs.pipenv.org/](https://docs.pipenv.org/)

## (Mac) Instalación con Homebrew

Se utilizarán los comandos de mac con homebrew [https://brew.sh/](https://brew.sh/)

```bash

brew install python && brew install pipenv

```

Asegurar de que el entorno esté configurado en `.bashrc` o `.zshrc`

```bash

export LC_ALL=es_ES.UTF-8
export LANG=es_ES.UTF-8
export PATH=/usr/local/bin:/usr/local/sbin:$PATH

```

### Nota

Si se quiere dejar a python3 como comando predeterminado se puede usar un alias.
Esto es solamente recomendado si por alguna razón no funciona exportar el `PATH`
con `/usr/local/bin` antes de los comandos del sistema.

```bash

alias python=python3
alias pip=pip3
```

## (Unix) Instalacion con Pipsi

- Pipsi  [https://github.com/mitsuhiko/pipsi](https://github.com/mitsuhiko/pipsi)
- Pew [https://github.com/berdario/pew](https://github.com/berdario/pew)

Asegurar que se tenga instalado virtualenv

```bash
pip3 install --upgrade virtualenv
```

### Instalar Pipsi

```bash

curl https://raw.githubusercontent.com/mitsuhiko/pipsi/master/get-pipsi.py | python3 - --src 'git+https://github.com/mitsuhiko/pipsi.git'

```

Agregar la ruta de *pipsi* al PATH en `.bashrc` o `.zshrc`

```bash

export LC_ALL=es_ES.UTF-8
export LANG=es_ES.UTF-8
export PATH=/home/<user>/.local/bin:$PATH

```

Instalar *pipenv* y *pew*

```bash

pipsi install pipenv
pipsi install pew

```

### Nota

También es posible utilizando pip3 normalmente

```bash

pip3 install pipenv

```

## Ejecución

Se debe ejecutar el comando

```bash

pipenv install && pipenv shell

```

Para poder instalar las dependencias y habilitar el entorno.

Luego se debe configuar el archivo `.env`

```bash

cp env.example .env
vim .env

```

Finalmente ejecutar el bot con

```bash

python3 .

```

## Editor Recomendado

El editor de código recomendado es PyCharm [https://www.jetbrains.com/pycharm/](https://www.jetbrains.com/pycharm/)
edición comunitaria. Otra alternativa es Ninja Ide [http://ninja-ide.org/](http://ninja-ide.org/).

## Paquetes Usados
Los paquetes utilizados para crear el esqueleto del bot son los siguientes:

- Python Telegram Bot [https://python-telegram-bot.readthedocs.io](https://python-telegram-bot.readthedocs.io): Framework de Bots para Telegram
- Emoji [https://github.com/carpedm20/emoji](https://github.com/carpedm20/emoji): Funciones para trabajar con emojis

- Events [http://events.readthedocs.io/en/latest/](http://events.readthedocs.io/en/latest/) Sistema para crear y gatillar eventos
- Unipath [https://github.com/mikeorr/Unipath](https://github.com/mikeorr/Unipath): Funciones para manejo de rutas

- EnvParse [https://github.com/rconradharris/envparse](https://github.com/rconradharris/envparse): Archivos de configuración DotEnv
- JsonLogger [https://github.com/madzak/python-json-logger](https://github.com/madzak/python-json-logger): Formato del Logger para almacenar Json

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

- Python Telegram Bot [https://python-telegram-bot.readthedocs.io](https://python-telegram-bot.readthedocs.io): Framework de Bots para Telegram
- Emoji [https://github.com/carpedm20/emoji](https://github.com/carpedm20/emoji): Funciones para trabajar con emojis

### Comunicación

- Requests [http://docs.python-requests.org/](http://docs.python-requests.org/) : LLamadas a servicios webservice REST
- ParsePy [https://github.com/milesrichardson/ParsePy](https://github.com/milesrichardson/ParsePy) : API para Parseplatform.org
- Socket.io [http://python-socketio.readthedocs.io](http://python-socketio.readthedocs.io): Implementación de WebSockets
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
- Events [http://events.readthedocs.io/en/latest/](http://events.readthedocs.io/en/latest/) Sistema para crear y gatillar eventos
- PyFileSystem [https://www.pyfilesystem.org/](https://www.pyfilesystem.org/): Funciones para manejo de rutas y archivos
- Unipath [https://github.com/mikeorr/Unipath](https://github.com/mikeorr/Unipath): Funciones para manejo de rutas
- Natural Language [http://www.nltk.org/](http://www.nltk.org/) : Procesamiento de escritura e identificación de conceptos
- PyOTP [https://github.com/pyotp/pyotp](https://github.com/pyotp/pyotp) : Identificación de 2 factores

### Almacenamiento y Validación

- Redis (https://pypi.python.org/pypi/redis)
- PonyOrm (https://ponyorm.com/)
- Pewee [https://github.com/coleifer/peewee](https://github.com/coleifer/peewee): ORM simple
- Blitz (http://blitzdb.readthedocs.io/en/latest/)
- Cerberus [http://docs.python-cerberus.org/](http://docs.python-cerberus.org/): Validación de Parámetros
- DiskCache (http://www.grantjenks.com/docs/diskcache/)
- Keyring [https://github.com/jaraco/keyring](https://github.com/jaraco/keyring): Almacenamiento de contraseñas seguro

### Configuración

- EnvParse [https://github.com/rconradharris/envparse](https://github.com/rconradharris/envparse): Archivos de configuración DotEnv
- JsonLogger [https://github.com/madzak/python-json-logger](https://github.com/madzak/python-json-logger): Formato del Logger para almacenar Json
- SimpleJson (https://simplejson.readthedocs.io/en/latest/)
- HJson (https://github.com/hjson/hjson-py)


### Herramientas para Pruebas

- The (http://the-py.github.io/the/)
- Green (https://github.com/CleanCut/green)
- Flake8 (http://flake8.pycqa.org)
- FactoryBoy (https://github.com/FactoryBoy/factory_boy)
