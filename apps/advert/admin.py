from django.contrib import admin
#my imports
from apps.advert import models

# Register your models here.
class BigAdvertFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'sub_title')
    search_fields = ('title', 'sub_title')

class NormalAdvertFilterAdmin(admin.ModelAdmin):
    list_filter = ('image', )
    list_display = ('image', 'url_booking')
    search_fields = ('image', 'url_booking')

class SmallAdvertFilterAdmin(admin.ModelAdmin):
    list_filter = ('image', )
    list_display = ('image', 'url_booking')
    search_fields = ('image', 'url_booking')
    
admin.site.register(models.BigAdvert, BigAdvertFilterAdmin)
admin.site.register(models.NormalAdvert, NormalAdvertFilterAdmin)
admin.site.register(models.SmallAdvert, SmallAdvertFilterAdmin)



