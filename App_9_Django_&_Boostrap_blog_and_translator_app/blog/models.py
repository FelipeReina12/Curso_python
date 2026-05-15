from django.db import models
from django.contrib.auth.models import User  # Importamos el modelo de usuario de Django para relacionarlo con el autor de la publicación

STATUS = ((0, 'Draft'), (1, 'Publish'))  # Definimos una tupla de opciones para el campo de estado de la publicación 
# Create your models here.
class Post(models.Model):  # Model es la clase que representa una tabla en la base de datos.
    title = models.CharField(max_length=200)  # CharField es un campo de texto con un límite de caracteres.
    content = models.TextField()  # TextField es un campo de texto sin límite de caracteres.
    date_created = models.DateTimeField(auto_now_add=True)  # DateTimeField es un campo de fecha y hora. 
    #auto_now_add=True hace que se establezca automaticamente la hora de creación de la publicación.
    slug = models.SlugField(max_length=200, unique=True)  # SlugField es un campo de texto que se utiliza para crear URLs amigables. 
    #unique=True hace que el valor del slug sea únco en la base de datos.
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)  # ForeignKey es un campo que crea una relación de clave foránea con otro modelo.
    #to=User indica que la relación es con el modelo de usuario de Django.
    #on_delete=models.CASCADE hace que si el usuario es eliminado, también se eliminen todas sus publicaciones.
    status = models.IntegerField(choices=STATUS, default=0)  # IntegerField es un campo de numero entero.
    #choices=STATUS hace que el campo solo pueda tomar los valores definidos en la tupla STATUS. 