
# Imagen_personal

paso 1  instalar django :  pip install Django

paso 2 configurar django en python:
    PS C:\Users\casa\Desktop\Imagen_personal> python
    Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import django  
    >>> django.VERSION
    (3, 2, 9, 'final', 0)
    >>> quit;

paso 3 inicializar proyecto : python -m django startproject ImagenParaTodas

==========================================================
- en el archivo settings.py , hay que setear la ruta donde estan las templates :
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["C:/Users/casa/Desktop/Imagen_personal/ImagenParaTodas/ImagenParaTodas/templates"],
 
- crear la app : python manage.py startapp Imagen

- agregar la app en el settings.py:

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'AppImagenParaTodas',
]

- checkear que todo venga bien con el comando:  

     python manage.py check AppImagenParaTodas

- luego crear la base de datos dentro de la carpeta que se creo de la app como models.py

- luego ejecutar el comando makemigrations para crear las clases propias previo a la migracion a la base de datos db.sqlite3: 

PS C:\Users\casa\Desktop\Imagen_personal\ImagenParaTodas> python manage.py makemigrations
Migrations for 'AppImagenParaTodas':
  AppImagenParaTodas\migrations\0001_initial.py
    - Create model Cuerpo
    - Create model Tip
    - Create model Vestido

- ejecutar el comando python manage.py sqlmigrate AppImagenParaTodas 0001 para crear revisar los script que se van a ejecutar en la base de datos:

PS C:\Users\casa\Desktop\Imagen_personal\ImagenParaTodas> python manage.py sqlmigrate AppImagenParaTodas 0001

- ejecutar python manage.py migrate para impactar los script en la base de datos db.sqlite3

PS C:\Users\casa\Desktop\Imagen_personal\ImagenParaTodas> python manage.py migrate
Operations to perform:
  Apply all migrations: AppImagenParaTodas, admin, auth, contenttypes, sessions
Running migrations:
  Applying AppImagenParaTodas.0001_initial... OK
  Applying contenttypes.0001_initial... OK


  