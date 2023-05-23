from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField

# Create your models here.
class Cancion(models.Model):
    TONOS = (
        ("C", "C"),
        ("C#", "C#"),
        ("D", "D"),
        ("D#", "D#"),
        ("E", "E"),
        ("F", "F"),
        ("F#", "F#"),
        ("G", "G"),
        ("G#", "G#"),
        ("A", "A"),
        ("A#", "A#"),
        ("B", "B")
    )

    titulo = models.CharField(max_length=200)
    tono = models.CharField(
        max_length = 2,
        choices = TONOS,
        default = "C" 
        )
    letra = RichTextField()

    def __str__(self):
        return self.titulo