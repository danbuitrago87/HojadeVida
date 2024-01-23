from django.db import models

# Create your models here.
class Project (models.Model):
    title=models.CharField(max_length=200, verbose_name='Título')
    description=models.TextField(verbose_name='Descripción')
    image=models.ImageField(verbose_name='Imagen', upload_to='projects')
    link=models.URLField(null=True, blank=True, verbose_name='link')                                           #se agrega un enlace
    created=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')     #se añade el campo automaticamente cuando se crea por 1vez
    updated=models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')         #se añade el campo automaticamente cuando se actualiza una instancia

    class Meta: 
        verbose_name='proyecto'                         #se cambia en el admin de django Project por proyecto
        verbose_name_plural='proyectos'                 #se cambia en el admin de django Projects por proyectos
        ordering=['-created']                           #se organizan los proyectos del más nuevo al más antiguo -created

    def __str__(self):                                  #se redefine el método str para devolver una cadena con el nombre del proyecto
        return self.title