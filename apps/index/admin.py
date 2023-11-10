from django.contrib.auth.models import User, Group
from django.contrib import admin
#my imports 
from apps.index import models

class SettingsFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'descriptions')
    search_fields = ('title', 'descriptions')

class AboutFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'descriptions')
    search_fields = ('title', 'descriptions')
    
class BannerFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', )
    search_fields = ('title', )


admin.site.unregister(Group) 
admin.site.register(models.Settings, SettingsFilterAdmin)
admin.site.register(models.About, AboutFilterAdmin)
admin.site.register(models.Banner, BannerFilterAdmin)

admin.site.site_header = "Vizitka.KG"  # Заголовок
admin.site.site_title = "Vizitka.KG Admin Portal"  # Титул
admin.site.index_title = "Добро пожаловать в портал администратора"  # Заголовок на главной странице