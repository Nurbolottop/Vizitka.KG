from django.contrib import admin
#my imports
from apps.blog import models

# Register your models here.
class BlogFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'sub_title')
    search_fields = ('title', 'sub_title')

class CategoryFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title',)
    search_fields = ('title',)
    
class StoriesFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title',)
    search_fields = ('title',)
    
admin.site.register(models.Blog, BlogFilterAdmin)
admin.site.register(models.Category, CategoryFilterAdmin)
admin.site.register(models.Stories, StoriesFilterAdmin)


