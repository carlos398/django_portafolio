from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField

#python manage.py createsuper user se usa para el usuario admin
# recuerda hacer las migraciones
# Create your models here.
class Project(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=250)
    image = ImageField(upload_to='portfolio/images/') #requiere instalar pillow
    url = URLField(blank=True)

# primero aca luego a admin