from django.contrib import admin
from . models import *


class categoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(category, categoryAdmin)

# Register your models here.

class productAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(product, productAdmin)