from django.contrib import admin
from .models import Band
from .models import Singers


class BandAdmin(admin.ModelAdmin):  # we insert these two lines...
    list_display = ('title', 'year_formed', 'genre', 'singer')  # list the fields we want on the list display


class SingersAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Band, BandAdmin)  # we edit this line, adding a second argument

admin.site.register(Singers, SingersAdmin)

# Register your models here.
