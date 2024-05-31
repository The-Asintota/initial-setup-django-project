# {{ cookiecutter.project_name }}
> [!NOTE]
> Este proyecto aun está en desarrollo.


## 1. Descripción del proyecto


## 2. Estructura
La estructura del proyecto es la siguiente:

```
└── 📁{{ cookiecutter.project_name }}
    └── 📁settings
        └── 📁environments
            └── base.py
            └── development.py
            └── production.py
            └── testing.py
        └── asgi.py
        └── urls.py
        └── wsgi.py
    └── 📁apps
    └── manage.py
└── 📁tests
└── pyproject.toml
└── poetry.lock
```

- **[{{ cookiecutter.project_name }}](./{{ cookiecutter.project_name }}/):** Este es el directorio raíz del poryecto. Contiene todos los modulos y configuraciones  globales.

- **[apps](./{{ cookiecutter.project_name }}/apps/):** Este directorio contiene las aplicaciones Dajngo. Está dividido en varios subdirectorios, cada uno de los cuales representa un servicio o aplicación. Tambien podras encontras algunos ficheros auxiliares en donde cada servicio podra hacer uso de ellos respectivamente.

- **[settings](./{{ cookiecutter.project_name }}/settings/):** Contiene archivos de configuración. Incluye configuraciones para los diferentes entornos de desarrollo, producción y pruebas, configuraciones de las rutas del proyecto, configuraciones ASGI y WSGI, etc.

- **[tests](./tests/):** Contiene pruebas unitarias y de implementación del código de cada aplicación.

- **[manage.py](./{{ cookiecutter.project_name }}/manage.py):** Esta es una utilidad de línea de comandos que te permite interactuar con tu proyecto Django de varias maneras.

- **[pyproject.toml](./pyproject.toml):** Este archivo es de configuración para un proyecto de Python que utiliza Poetry para la gestión y el empaquetado de dependencias.

## 3. Tecnologías


## 4. Instalación del proyecto
Primero debes seguir las siguientes instrucciones y dependiendo de que manera quieres realizar la instalación seguiras los pasos para instalar el proyecto de manera manual o utilizando Docker.

- **Clonar repositorio:** Para clonar este repositorio ejecuta los siguientes comandos.
    
    ```bash
    git clone {{ cookiecutter.repository }}
    ```
    
- **Crear y activar entorno virtual:** Creares un entorno virtual con el siguiente comando, en este entorno instalaremos todas las dependencias de este proyecto.
    
    ```bash
    poetry shell
    ```
    
- **Configurar variables de entorno:** Crea un archivo con el nombre _.env_ dentro del directorio _src_. En este archivo se definiran todas las variables de entorno de este proyecto. Las variables que se deben configurar son las siguientes.

    ```.env
    # DJANGO
    KEY_DJANGO=<value>

    # CLIENTS
    BACKEND_HOST=<host_server_backend>
    FRONTEND_HOST=<host_server_frontend>
    ```

    El valor de la variable `KEY_DJANGO` lo puedes obtener ejecutando los siguientes comandos. Primero iniciamos el intérprete de Python.

    ```bash
    python3
    ```

    El siguiente comando te va retornar el valor de `KEY_DJANGO` que deberas copiar en el archivo _.env_.

    ```bash
    from django.core.management.utils import get_random_secret_key; print(get_random_secret_key()); exit()
    ```

    Para el envío de mensajes a través de correo electrónico tienes que tener una contraseña de aplicación que permita al sistema de gestión inmobiliario autenticarse y poder utilizar el servicio de mensajería.

### 4.1. Instalación manual

- **Paso 1 (instalar dependencias):** Para instalar las teconologias y paquetes que usa el proyecto usa el siguiente comando. Asegurate estar en el directotio raíz.
    
    ```bash
    poetry install
    ```
    
- **Paso 2 (realizar migraciones):** Migramos los modelos del proyecto necesarios para el funcionamiento del servidor con el siguiente comando.
    
    ```bash
    python3 {{ cookiecutter.project_name }}/manage.py migrate --settings=settings.environments.development
    ```

- **Paso 3 (iniciar el servidor):** Para iniciar el servidor de manera local ejecuta el siguiente comando.
    
    ```bash
    python3 {{ cookiecutter.project_name }}/manage.py runserver --settings=settings.environments.development
    ```
    
### 4.2. Instalación con Docker


## 5. Tests
Para correr las pruebas del proyecto debes ejecutar el siguiente comando.

```bash
pytest {{ cookiecutter.project_name }}/tests/
```

## 6. Contributores
Si está interesado en contribuir a este proyecto, consulte nuestra guía [CONTRIBUTING](CONTRIBUTING.md) para obtener información sobre cómo comenzar. Proporciona pautas sobre cómo configurar su entorno de desarrollo, proponer cambios y más. ¡Esperamos sus contribuciones!

## 7. Colaboradores
