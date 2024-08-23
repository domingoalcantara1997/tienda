
from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Producto
from django.contrib import messages
from .serializers import ProductoSerializer
from django.views.generic.edit import CreateView

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer