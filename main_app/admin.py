from django.contrib import admin
from .models import Bird # import the Artist model from models.py
# Register your models here.

admin.site.register(Bird) # this line will add the model to the admin panel