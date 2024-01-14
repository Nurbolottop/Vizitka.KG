from django.contrib import admin
from apps.blog import models

# Register your models here.
class CategoryFilterAdmin(admin.ModelAdmin):
    verbose_name_plural = 'Категории'
    list_filter = ('title', )
    list_display = ('title',)
    search_fields = ('title',)

class BlogFilterAdmin(admin.ModelAdmin):
    verbose_name_plural = 'Новости'
    list_filter = ('title', )
    list_display = ('title', 'sub_title')
    search_fields = ('title', 'sub_title')

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

class MagazineFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'price')
    search_fields = ('title', 'price')

class SiteFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'price')
    search_fields = ('title', 'price')

class BannerFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title',)
    search_fields = ('title',)

admin.site.register(models.Category, CategoryFilterAdmin)
admin.site.register(models.Blog, BlogFilterAdmin)
admin.site.register(models.BigAdvert, BigAdvertFilterAdmin)
admin.site.register(models.NormalAdvert, NormalAdvertFilterAdmin)
admin.site.register(models.SmallAdvert, SmallAdvertFilterAdmin)
admin.site.register(models.Magazine, MagazineFilterAdmin)
admin.site.register(models.Site, SiteFilterAdmin)
admin.site.register(models.Banner, BannerFilterAdmin)


