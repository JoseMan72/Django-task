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

## Paso 6: Creamos la aplicación

```bash
python manage.py startapp tasks
```

## Paso 7: Registramos la aplicación en settings.py

```python
INSTALLED_APPS = [
    ...
    'tasks',
]
```

## Paso 8: Creamos el modelo

Añadimos el siguiente código en models.py después del comentario

```python
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
```

## Paso 9: Aplicamos los cambios en la base de datos

```bash
python manage.py makemigrations
python manage.py migrate
```

## Paso 10: Registramos el modelo

```python
from django.contrib import admin
from .models import Task

admin.site.register(Task)
```

## Paso 11: Creamos el superusuario

```bash
python manage.py createsuperuser
```

## Paso 12: Creamos la vista

```python
from django.shortcuts import render
from .models import Task

def index(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})
```

## Paso 13: Registramos la vista

Creamos el archivo urls.py en la carpeta tasks y añadimos el siguiente código

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
]
```

Añadimos la ruta en urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),
]
```

## Paso 14: Creamos la plantilla

Creamos la carpeta templates y dentro de ella la carpeta tasks. Creamos el archivo task_list.html, debería quedar así tasks/templates/tasks/task_list.html

En task_list.html añadimos el siguiente código

```html
<!DOCTYPE html>
<html lang="es">
	<head>
		<meta charset="UTF-8" />
		<title>Task List</title>
	</head>
	<body>
		<h1>Task List</h1>
		<ul>
			{% for task in tasks %}
			<li>
				{{ task.title }} - {{ task.description }} - 
				{{ task.completed|yesno:"Realizado,Pendiente" }}
			</li>
			{% empty %}
			<li>No hay tareas por hacer.</li>
			{% endfor %}
		</ul>
	</body>
</html>
```
