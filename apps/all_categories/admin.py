from django.contrib import admin
from apps.all_categories import models
# Register your models here.
    
class D1BlogFilterAdmin(admin.ModelAdmin):
    list_filter = ('first', )
    list_display = ('first',)
    search_fields = ('first',)    
class D2BlogFilterAdmin(admin.ModelAdmin):
    list_filter = ('second', )
    list_display = ('second',)
    search_fields = ('second',)    
class D3BlogFilterAdmin(admin.ModelAdmin):
    list_filter = ('third', )
    list_display = ('third',)
    search_fields = ('third',)
    
admin.site.register(models.D1Blog,D1BlogFilterAdmin)
admin.site.register(models.D2Blog,D2BlogFilterAdmin)
admin.site.register(models.D3Blog,D3BlogFilterAdmin)


#B - Base

class B1BlogFilterAdmin(admin.ModelAdmin):
    list_filter = ('first', )
    list_display = ('first', )
    search_fields = ('first', )  # Замените search_display на search_fields

class B2BlogFilterAdmin(admin.ModelAdmin):
    list_filter = ('second', )
    list_display = ('second', )
    search_fields = ('second', )

class B3BlogFilterAdmin(admin.ModelAdmin):
    list_filter = ('third', )
    list_display = ('third', )
    search_fields = ('third', )
    
class B4BlogFilterAdmin(admin.ModelAdmin):
    list_filter = ('four', )
    list_display = ('four', )
    search_fields = ('four', )

class B5BlogFilterAdmin(admin.ModelAdmin):
    list_filter = ('five_one', )
    list_display = ('five_one', )
    search_fields = ('five_one', )

class B6BlogFilterAdmin(admin.ModelAdmin):
    list_filter = ('five_two', )
    list_display = ('five_two', )
    search_fields = ('five_two', )

class B7BlogFilterAdmin(admin.ModelAdmin):
    list_filter = ('five_three', )
    list_display = ('five_three', )
    search_fields = ('five_three', )       

admin.site.register(models.B1Blog, B1BlogFilterAdmin)
admin.site.register(models.B2Blog, B2BlogFilterAdmin)
admin.site.register(models.B3Blog, B3BlogFilterAdmin)
admin.site.register(models.B4Blog, B4BlogFilterAdmin)
admin.site.register(models.B5Blog, B5BlogFilterAdmin)
admin.site.register(models.B6Blog, B6BlogFilterAdmin)
admin.site.register(models.B7Blog, B7BlogFilterAdmin)
