# Bot Template

Es la base para crear bots de telegram.

## Requerimientos

- Python 3.6+
- PipEnv [https://docs.pipenv.org/](https://docs.pipenv.org/)

## Configurar Archivo .env

Se debe configuar el archivo `.env` dentro de `src/`
con las claves dadas por el [Botfather](https://core.telegram.org/bots)

```bash

cp env.example .env
vim .env

```

Establecer `BOT_TELEGRAM_KEY=""` y para ejecutar el bot con

```bash

python3 .

```

## Instalación con Docker

Se ha utilizado [Docker Compose](https://docs.docker.com/compose/install/#install-compose) para poder
crear un ambiente de desarrollo.

### Instalación y Ejecución

```sh
docker-compose build

docker-compose up -d
```

Ver logs:  `docker logs telegram-bot`

## (Mac) Instalación con Homebrew

Se utilizarán los comandos de mac con homebrew [https://brew.sh/](https://brew.sh/)

```bash

brew install python && brew install pipenv

```

Asegurar de que el entorno esté configurado en `.bashrc` o `.zshrc`

```bash
export PATH=/usr/local/bin:/usr/local/sbin:$PATH
```

## Instalación con pip

También es posible utilizando pip3 normalmente

```bash

pip3 install pipenv

```

## Ejecución

Asegurar de que las variables de idioma estén en el entorno

```bash
export LC_ALL=C.UTF-8
export LANG=C.UTF-8
```

Luego se debe ejecutar el comando

```bash

pipenv install && pipenv shell

```

Para poder instalar las dependencias y habilitar el entorno.

## Editor Recomendado

El editor de código recomendado es PyCharm [https://www.jetbrains.com/pycharm/](https://www.jetbrains.com/pycharm/)
edición comunitaria. Otra alternativa es Ninja Ide [http://ninja-ide.org/](http://ninja-ide.org/).

## Materiales Recomendados

- [http://goalkicker.com/](http://goalkicker.com/)
- [Libro de Python](http://goalkicker.com/PythonBook)
- [Libro de Git](http://goalkicker.com/GitBook)
- [Libro de Linux](http://goalkicker.com/LinuxBook)
- [Documentación Bots de Telegram](https://core.telegram.org/bots)

## Paquetes Usados
Los paquetes utilizados para crear el esqueleto del bot son los siguientes:

- Python Telegram Bot [https://python-telegram-bot.readthedocs.io](https://python-telegram-bot.readthedocs.io): Framework de Bots para Telegram
- Emoji [https://github.com/carpedm20/emoji](https://github.com/carpedm20/emoji): Funciones para trabajar con emojis

- Events [http://events.readthedocs.io/en/latest/](http://events.readthedocs.io/en/latest/): Sistema para crear y gatillar eventos
- Unipath [https://github.com/mikeorr/Unipath](https://github.com/mikeorr/Unipath): Funciones para manejo de rutas

- EnvParse [https://github.com/rconradharris/envparse](https://github.com/rconradharris/envparse): Archivos de configuración DotEnv
- JsonLogger [https://github.com/madzak/python-json-logger](https://github.com/madzak/python-json-logger): Formato del Logger para almacenar Json

## Crear Comandos

El bot tiene una estructura que permite crear nuevos comandos de forma simple.
Cada comando debe tener como mínimo dos archivos.

Estos archivos deben estar dentro de un directorio con el nombre del comando
dentro de [bot/commands](bot/commands)

`directorio/`

- `__init__.py` : Debe tener clase `Command` Subclase de `BaseCommand`. Almacena datos generales del comando.
- `controller.py`: Debe tener clase `Controller` Subclase de `BaseController`. Ejecuta la lógica y coordina con los otros componentes.

El bot cargará el comando automáticamente. Si se desea deshabilitar un comando
se debe agregar el directorio a la lista de comandos deshabilitados en `__main__.py`

Los archivos opcionales de cada comando son los siguientes:

- `view.py`: Almacena los mensajes que el bot puede entregar como respuesta
- `requester.py`: Se encarga de realizar los llamados a los webservices y api rest
- `model.py`: Se encarga de interactuar con las base de datos u otro tipo de almacenamiento
- `validator.py`: Se encarga de validar y sanitizar los parámetros de entrada


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

- Requests [http://docs.python-requests.org/](http://docs.python-requests.org/) : Llamadas a servicios webservice REST
- ParsePy [https://github.com/milesrichardson/ParsePy](https://github.com/milesrichardson/ParsePy) : API para Parseplatform.org
- Socket.io [http://python-socketio.readthedocs.io](http://python-socketio.readthedocs.io): Implementación de WebSockets
- Json API Requests [https://github.com/socialwifi/jsonapi-requests](https://github.com/socialwifi/jsonapi-requests): Funciones para interactuar con servicios web que implementen el estándar Json API.
- Python JWT [https://github.com/davedoesdev/python-jwt](https://github.com/davedoesdev/python-jwt): Permite generar y validar Jason Web Tokens [https://jwt.io](https://jwt.io)

### Utilidades

- Jinja2 [http://jinja.pocoo.org/](http://jinja.pocoo.org/): Sistema de templates
- Babel [http://babel.pocoo.org](http://babel.pocoo.org): Sistema de traducción e internacionalización
- Money [https://github.com/vimeo/py-money)](https://github.com/vimeo/py-money): Sistema de transformación de divisas
- Flufli18n [https://flufli18n.readthedocs.io](https://flufli18n.readthedocs.io): Sistema de traducción
- Arrow [https://arrow.readthedocs.io/en/latest/](https://arrow.readthedocs.io/en/latest/): Permite mejorar el manejo de hora y fecha
- Crython [https://github.com/ahawker/crython](https://github.com/ahawker/crython): Permite ejecutar funciones dependiendo de un tiempo similar a cron
- Promises [https://github.com/syrusakbary/promise](https://github.com/syrusakbary/promise): Implementa el estandar de promesas
- Events [http://events.readthedocs.io/en/latest/](http://events.readthedocs.io/en/latest/): Sistema para crear y gatillar eventos
- PyFileSystem [https://www.pyfilesystem.org/](https://www.pyfilesystem.org/): Funciones para manejo de rutas y archivos
- Unipath [https://github.com/mikeorr/Unipath](https://github.com/mikeorr/Unipath): Funciones para manejo de rutas
- Natural Language [http://www.nltk.org/](http://www.nltk.org/) : Procesamiento de escritura e identificación de conceptos
- PyOTP [https://github.com/pyotp/pyotp](https://github.com/pyotp/pyotp) : Identificación de 2 factores
- Tablib [https://github.com/kennethreitz/tablib](https://github.com/kennethreitz/tablib): Creación de datos tabulados y otros formatos
- PwnedApi [https://github.com/nikoheikkila/pwnedapi](https://github.com/nikoheikkila/pwnedapi): Permite saber la cantidad de veces que una contraseña fue hackeada.
- Parse [https://pypi.python.org/pypi/parse](https://pypi.python.org/pypi/parse): Permite extraer información de strings.
- Docopt [https://github.com/docopt/docopt](https://github.com/docopt/docopt): Facilita el uso de comandos de terminal.

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


### Herramientas para control de calidad

- The [http://the-py.github.io/the/](http://the-py.github.io/the/)
- Green [https://github.com/CleanCut/green](https://github.com/CleanCut/green)
- Flake8 [http://flake8.pycqa.org](http://flake8.pycqa.org)
- FactoryBoy [https://github.com/FactoryBoy/factory_boy](https://github.com/FactoryBoy/factory_boy)
- Mypy [http://mypy.readthedocs.io/en/latest/introduction.html](http://mypy.readthedocs.io/en/latest/introduction.html)
