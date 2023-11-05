from django.contrib import admin
from apps.category import models

class FirstBlogFilterAdmin(admin.ModelAdmin):
    list_filter = ('first', )
    list_display = ('first', )
    search_fields = ('first', )  # Замените search_display на search_fields

class SecondBlogFilterAdmin(admin.ModelAdmin):
    list_filter = ('second', )
    list_display = ('second', )
    search_fields = ('second', )

class ThirdBlogFilterAdmin(admin.ModelAdmin):
    list_filter = ('third', )
    list_display = ('third', )
    search_fields = ('third', )
    
class FourBlogFilterAdmin(admin.ModelAdmin):
    list_filter = ('four', )
    list_display = ('four', )
    search_fields = ('four', )

class FiveOneBlogFilterAdmin(admin.ModelAdmin):
    list_filter = ('five_one', )
    list_display = ('five_one', )
    search_fields = ('five_one', )

class FiveTwoBlogFilterAdmin(admin.ModelAdmin):
    list_filter = ('five_two', )
    list_display = ('five_two', )
    search_fields = ('five_two', )

class FiveThreeBlogFilterAdmin(admin.ModelAdmin):
    list_filter = ('five_three', )
    list_display = ('five_three', )
    search_fields = ('five_three', )       

admin.site.register(models.FirstBlog, FirstBlogFilterAdmin)
admin.site.register(models.SecondBlog, SecondBlogFilterAdmin)
admin.site.register(models.ThirdBlog, ThirdBlogFilterAdmin)
admin.site.register(models.FourBlog, FourBlogFilterAdmin)
admin.site.register(models.FiveOneBlog, FiveOneBlogFilterAdmin)
admin.site.register(models.FiveTwoBlog, FiveTwoBlogFilterAdmin)
admin.site.register(models.FiveThreeBlog, FiveThreeBlogFilterAdmin)
