from django.contrib import admin
from home.models import *
# Register your models here.

class booktableAdmin(admin.ModelAdmin):
    list_display=('Name','Email','Time','Date')

admin.site.register(booktable,booktableAdmin)

class signupdetailsAdmin(admin.ModelAdmin):
    list_display=('Email','Password')

admin.site.register(signupdetails,signupdetailsAdmin)