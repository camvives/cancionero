from django.db import models
from django.utils.translation import gettext_lazy as _
import re

# Create your models here.
class Cancion(models.Model):
    titulo = models.CharField(max_length=200)
    letra = models.TextField()
    nro_sp = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.titulo
    
    def subir_medio(self):
        replacements = {
            'G#': 'A',
            'A#': 'B',
            'C#': 'D',
            'D#': 'E',
            'F#': 'G',
            'Ab': 'A',
            'Bb': 'B',
            'Db': 'D',
            'Eb': 'E',
            'Gb': 'G',
            'A': 'Bb',
            'B': 'C',
            'C': 'C#',
            'D': 'D#',
            'E': 'F',
            'F': 'F#',
            'G': 'G#',
            }

        pattern =  re.compile(r'\*(.*?)\*')
        result = pattern.sub(lambda x: '*' + replacements.get(x.group(1), x.group(1)) + '*', self.letra)
        self.letra = result 
    
    def bajar_medio(self):
        replacements = {
            'G#': 'G',
            'A#': 'A',
            'C#': 'C',
            'D#': 'D',
            'F#': 'F',
            'Ab': 'G',
            'Bb': 'A',
            'Db': 'C',
            'Eb': 'D',
            'Gb': 'F',
            'A': 'G#',
            'B': 'Bb',
            'C': 'B',
            'D': 'C#',
            'E': 'D#',
            'F': 'E',
            'G': 'F#',
        }

        pattern =  re.compile(r'\*(.*?)\*')
        result = pattern.sub(lambda x: '*' + replacements.get(x.group(1), x.group(1)) + '*', self.letra)
        self.letra = result

class Setlist(models.Model):
    titulo = models.CharField(max_length=200)
    canciones = models.ManyToManyField(Cancion)

    def __str__(self):
        return self.titulo