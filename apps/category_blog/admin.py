from django.contrib import admin
from apps.category_blog import models
# Register your models here.

class FirsNewsBlogFilterAdmin(admin.ModelAdmin):
    list_filter = ('first', )
    list_display = ('first', )
    search_display = ('first', )
    
    
admin.site.register(models.FirsNewsBlog, FirsNewsBlogFilterAdmin)
