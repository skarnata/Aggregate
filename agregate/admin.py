from django.contrib import admin
from .models import Country, City, Question, Choice

# Register your models here.
admin.site.register(Country)

admin.site.register(City)

admin.site.register(Question)

admin.site.register(Choice)
