from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    def validate_precio(self, value):
        if value < 100:
            raise serializers.ValidationError("El precio no puede ser menor de 100 pesos.")
        return value

    class Meta:
        model = Producto
        fields = '__all__'