## Activar el entorno virtual
comando: source env/Scripts/activate

# Crear nuevo proyecto Django
comando: django-admin startproject "mysite" .

Lo que está en comillas es como se va a llamar el proyecto

## Inicializar el proyecto 
comando: py manage.py runserver   
Después de ejecutar el comando, necesitamos ejecutar algunos comndos SQL como:
py manage.py migrate   
Esto nos crea una base de datos 

## Crear un usuario adeministrador 
para crear un superusuario se utiliza el comando:  
py manage.py createsuperuser

## Crear una aplicación para el proyecto en Django

Se utiliza el comando:  
py manage.py startapp blog. Esto nos crea la carperta con varios archivos y migraciones

Las migraciónes son un cambio en las bases de datos

En el archivo models.py se enecuentran las bases de datos de la página web 

## Agregar nuestra aplicación a las configuraciones de mysite
En la carpeta mysite ubicamos el archivo settings.py y donde está la lista INSTALLED_APPS en el ultimo campo agregamso el nombre de nuestra app

# Comenzando a desarrollar nuestra app

## Modelos 
En el archivo models.py organizamos los valores de la base de datos mediante la clase models   
Luego para aplicar ese modelo a la base de datos aplicamos los siguientes comandos:  
py manage.py makemigrations   
py manage.py migrate