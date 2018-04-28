from django.contrib import admin
from .models import Zoo, Exhibit, Animal
# Register your models here.
admin.site.register(Zoo)
admin.site.register(Animal)
admin.site.register(Exhibit)
