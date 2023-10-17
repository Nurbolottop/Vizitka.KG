from django.contrib import admin
#my imports
from apps.advert import models

# Register your models here.
class BigAdvertFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'sub_title')
    search_fields = ('title', 'sub_title')


    
admin.site.register(models.BigAdvert, BigAdvertFilterAdmin)


