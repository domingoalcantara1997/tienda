from django.db import models
from django.core.exceptions import ValidationError


def validate_precio(value):
    if value < 100:
        raise ValidationError('El precio no puede ser menor de 100 pesos.')

class Producto(models.Model):
    codigo = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2, validators=[validate_precio])
    TIPO_PRODUCTO = [
        ('local', 'Local'),
        ('internacional', 'Internacional')
    ]
    tipo = models.CharField(max_length=20, choices=TIPO_PRODUCTO)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)  # Campo para la imagen

    def __str__(self):
        return self.codigo