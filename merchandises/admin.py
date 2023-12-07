from django.contrib import admin

# Register your models here.
from .models import Category, Merchandise

admin.site.register(Category)
admin.site.register(Merchandise)