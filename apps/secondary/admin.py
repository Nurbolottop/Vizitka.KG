from django.contrib import admin
from apps.secondary import models

# Register your models here.
class TeamFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name', 'work')
    search_fields = ('name', 'work')

class HistoryFilterAdmin(admin.ModelAdmin):
    list_filter = ('year', )
    list_display = ('year', 'title')
    search_fields = ('year', 'title')
    

class StoriesFilterAdmin(admin.ModelAdmin):
    verbose_name_plural = 'Сторисы'
    list_filter = ('title', )
    list_display = ('title',)
    search_fields = ('title',)

class PartnersFilterAdmin(admin.ModelAdmin):
    verbose_name_plural = 'Партнеры'
    list_filter = ('title', )
    list_display = ('title',)
    search_fields = ('title',)
    
admin.site.register(models.Team, TeamFilterAdmin)
admin.site.register(models.History, HistoryFilterAdmin)
admin.site.register(models.Stories, StoriesFilterAdmin)
admin.site.register(models.Partners, PartnersFilterAdmin)

