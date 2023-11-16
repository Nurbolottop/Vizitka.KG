from django.contrib import admin
from apps.magazine import models

# Register your models here.
class MagazineFilterAdmin(admin.ModelAdmin):
    list_filter = ("title",)
    list_display = ("title",)
    search_fields = ("title",)

    
admin.site.register(models.Magazine, MagazineFilterAdmin)
# admin.site.register(models.MagazineImage)

