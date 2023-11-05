from django.contrib.auth.models import User, Group
from django.contrib import admin
#my imports 
from apps.index.models import Settings,Team

class SettingsFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'descriptions')
    search_fields = ('title', 'descriptions')

class TeamFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name', 'work')
    search_fields = ('name', 'work')
    
admin.site.unregister(Group) 
admin.site.register(Settings, SettingsFilterAdmin)
admin.site.register(Team, TeamFilterAdmin)