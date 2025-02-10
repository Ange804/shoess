from django.contrib import admin
from .models import chauss

class chaussAdmin(admin.ModelAdmin):
    list_display = ('name','prix','quantite')

admin.site.register(chauss, chaussAdmin)
