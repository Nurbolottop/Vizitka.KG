from django.contrib import admin
#my imports
from apps.blog import models

# Register your models here.
class BlogSubTextInline(admin.TabularInline):
    model = models.BlogSubTitle
    extra = 1

class BlogInfoTextInline(admin.TabularInline):
    model = models.BlogInfoText
    extra = 1

class BlogImageInline(admin.TabularInline):
    model = models.BlogImage
    extra = 1
    
class BlogFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'sub_title')
    search_fields = ('title', 'sub_title')
    inlines = [BlogSubTextInline,BlogInfoTextInline,BlogImageInline]

class CategoryFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title',)
    search_fields = ('title',)
       
    
admin.site.register(models.Blog, BlogFilterAdmin)
admin.site.register(models.Category, CategoryFilterAdmin)

