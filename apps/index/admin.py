from django.contrib.auth.models import User, Group
from django.contrib import admin
#my imports 
from apps.index.models import Settings

class SettingsFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'descriptions')
    search_fields = ('title', 'descriptions')

admin.site.unregister(User)
admin.site.unregister(Group) 
admin.site.register(Settings, SettingsFilterAdmin)
