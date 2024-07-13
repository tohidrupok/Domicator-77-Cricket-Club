from django.contrib import admin
from . models import *

class Playeradmin(admin.ModelAdmin): 
     list_display = ['name']    
     prepopulated_fields = {'slug' : ('name',)} 
     
admin.site.register(Player, Playeradmin)
admin.site.register(Home)
