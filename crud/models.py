from django.db import models
from django.utils import timezone

class Libro(models.Model):
    titulo = models.CharField(max_length=50)
    fecha_publicacion = models.DateField(null=True, default=timezone.now)
    autor = models.CharField(max_length=30, blank=True)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    paginas = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.titulo
