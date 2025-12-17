from django.contrib import admin
from .models import MyModel

# Register your models here.

class MyModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'email')
admin.site.register(MyModel, MyModelAdmin)

