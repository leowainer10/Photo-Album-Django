from django.contrib import admin
from .models import Photo, Category


admin.site.register(Category)
admin.site.register(Photo)