# Pasos

## Paso 1: Crear entorno virtual y activarlo

```bash
mkvirtualenv task
```

## Paso 2: Actualizar pip

```bash
python -m pip install -- upgrade pip
```

## Paso 2: Crear archivo requirements.txt e instalar dependencias

El archivo requirements.txt debe contener: Django~=4.2.7

```bash
pip install -r requirements.txt
```

## Paso 3: Crear proyecto Django

```bash
django-admin startproject task
```

## Paso 4: Configuración

En settings.py, vamos a cambiar la zona horaria y el idioma

```python
TIME_ZONE = 'Europe/Madrid'
LANGUAGE_CODE = 'es'
```

Añadimos las rutas de los archivos estáticos

```python
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'
```

Añadimos en ALLOWED_HOSTS la dirección de nuestro servidor

```python
ALLOWED_HOSTS = ['127.0.0.1']
```

Creamos e inicializamos la base de datos

```bash
python manage.py migrate
```

## Paso 5: Arrancamos el servidor

```bash
python manage.py runserver
```
