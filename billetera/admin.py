from django.contrib import admin
from .models import Balance, Categoria, Movimiento

# Register your models here.

admin.site.register(Balance)
admin.site.register(Categoria)
admin.site.register(Movimiento)