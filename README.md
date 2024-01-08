# VMSM

_repositorio de volume and merchandise management system  (sistema de gestión de volumenes y mercancias), el cual se trata de una aplicación web la cual esta construida y codificada en Python en conjunto al potente framework Django, el cual apoya para el rendimiento, gestion y administración de container/almacenes de la empresa, tomado en cuenta las reglas o normativa de negocios._

## Prerrequisitos

- Python version 3.8.x o superiores
- Paquetador de python (PIP)
- Tener el paquete de "virtualenv", en caso de no tenerlo correr el comando `pip install virtualenv`
- Conexion a una base de datos relacional, preferiblemente Postgres

## Comienzo

1. hacer un entorno virtual `virtualenv -p python env` en la carpeta del proyecto (VMSM)
2. entrar al entorno virtual `.\env\Scripts\activate`
3. instalar todas las dependecias del proyecto 
```
pip install -r requirements.txt
```
4. puedes revisar la versión de django con `python -m django --version`
5. Para hacer las migraciones, Primero cambiar las variables de entorno en un .env tomando como referencia el .env.sample, despues ejecurar los siguientes comandos:
    1. `python .\project\manage.py  makemigrations` 
    2. `python .\project\manage.py migrate appLogin 0002`
    3. `python .\project\manage.py migrate`
    4. (Opcional) Crear un super usuario con django `python .\project\manage.py createsuperuser` poner nombre de usuario,mail y dos veces contraseña.
6. Para levantar el servidor entrar en la carpeta "project" `python .\project\manage.py runserver`

## Despliegue

El repositorio tiene un flujo CI/CD, tanto con github actions y despliegue en _Render_, además de poder hacer despligue con docker con sus archivos 
```
dockerfile
```
```
docker-compose.yml
```

## Testing

El proyecto tiene testing del cual se hace uso del módulo de Django para el testing.

## Preview

![Ejemplo de aplicación en uso](https://github.com/wagnermorillo/VMSM/blob/main/screenshot.png)


