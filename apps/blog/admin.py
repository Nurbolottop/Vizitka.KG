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
    
# Category filter in BlogDetail
class FirstBlogDetailFilterAdmin(admin.ModelAdmin):
    list_filter = ('first', )
    list_display = ('first', )
    search_display = ('first', )
    
class SecondBlogDetailBlogFilterAdmin(admin.ModelAdmin):
    list_filter = ('second', )
    list_display = ('second', )
    search_display = ('second', )

class ThirdBlogDetailFilterAdmin(admin.ModelAdmin):
    list_filter = ('third', )
    list_display = ('third', )
    search_display = ('third', )
    
admin.site.register(models.FirstBlogDetail, FirstBlogDetailFilterAdmin)
admin.site.register(models.SecondBlogDetail, SecondBlogDetailBlogFilterAdmin)
admin.site.register(models.ThirdBlogDetail, ThirdBlogDetailFilterAdmin)




