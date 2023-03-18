from django.contrib import admin
from .models import *

# Register your models here.

class Roms(admin.ModelAdmin):
    list_display = ('rom_name','android',)

admin.site.register(Rom,Roms)

class Mods(admin.ModelAdmin):
    list_display = ('mod_name','mod_android',)

admin.site.register(Mod,Mods)


class Contacts(admin.ModelAdmin):
    list_display=('name',)
admin.site.register(Contact,Contacts)

class Comments(admin.ModelAdmin):
    list_display=('name',)
admin.site.register(Comment,Comments)