# 1. Plantilla de proyecto Django

Este repositorio proporciona una plantilla para crear el contenido base e inicial de un repositorio que contiene un proyecto Django. Se gestiona con la biblioteca [cookiecutter](https://www.cookiecutter.io/), que permite generar proyectos con plantillas predefinidas.

# 2. Estructura del proyecto

La plantilla sigue un diseño estructurado para facilitar la navegación y el mantenimiento. Aquí hay una descripción general:

- `{{ cookiecutter.project_name }}`: Contiene todos los archivos iniciales del repositorio.
- `{{ cookiecutter.project_name }}/{{ cookiecutter.project_name }}`: Modulo que contiene el código fuente del proyecto, dicho modulo contendra los siguientes submodulos y archivos:
    - `settings`: Contiene archivos de configuración, incluidas configuraciones para diferentes entornos de desarrollo, producción y pruebas, configuraciones de rutas de proyectos, configuraciones ASGI y WSGI, etc.
    - `apps`: Contiene aplicaciones de Django. Está dividido en varios subdirectorios, cada uno de los cuales representa un servicio o aplicación. Aquí también se pueden encontrar archivos auxiliares, que cada servicio puede utilizar respectivamente.
    - `manage.py`: esta es una utilidad de línea de comandos que te permite interactuar con tu proyecto Django de varias maneras.
- `{{ cookiecutter.project_name }}/tests`: Contiene pruebas unitarias y de implementación para el código de cada aplicación.