from django.contrib import admin
# my imports
from apps.category import models

# Register your models here.
class FirstBlogFilterAdmin(admin.ModelAdmin):
    list_filter = ('first', )
    list_display = ('first', )
    search_display = ('first', )
    
class SecondBlogFilterAdmin(admin.ModelAdmin):
    list_filter = ('second', )
    list_display = ('second', )
    search_display = ('second', )

class ThirdBlogFilterAdmin(admin.ModelAdmin):
    list_filter = ('third', )
    list_display = ('third', )
    search_display = ('third', )
    
class FourBlogFilterAdmin(admin.ModelAdmin):
    list_filter = ('four', )
    list_display = ('four', )
    search_display = ('four', )

class FiveOneBlogFilterAdmin(admin.ModelAdmin):
    list_filter = ('five_one', )
    list_display = ('five_one', )
    search_display = ('five_one', )

class FiveTwoBlogFilterAdmin(admin.ModelAdmin):
    list_filter = ('five_two', )
    list_display = ('five_two', )
    search_display = ('five_two', )
class FiveThreeBlogFilterAdmin(admin.ModelAdmin):
    list_filter = ('five_three', )
    list_display = ('five_three', )
    search_display = ('five_three', )       

admin.site.register(models.FirstBlog, FirstBlogFilterAdmin)
admin.site.register(models.SecondBlog, SecondBlogFilterAdmin)
admin.site.register(models.ThirdBlog, ThirdBlogFilterAdmin)
admin.site.register(models.FourBlog, FourBlogFilterAdmin)
admin.site.register(models.FiveOneBlog, FiveOneBlogFilterAdmin)
admin.site.register(models.FiveTwoBlog, FiveTwoBlogFilterAdmin)
admin.site.register(models.FiveThreeBlog, FiveThreeBlogFilterAdmin)



    