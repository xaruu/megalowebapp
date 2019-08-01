from django.db import models
from django.utils.text import slugify

# Create your models here.


class Episodio(models.Model):

    titulo = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=2000)
    video_url = models.CharField(max_length=2000)
    slug = models.SlugField(editable=False, default="")

    class Meta:
        verbose_name = "Episodio"
        verbose_name_plural = "Episodios"

    def __str__(self):
        return self.titulo

    def save(self):
    	self.slug = slugify(self.titulo)
    	super().save()