from django.contrib import admin
from  .models import User,Subscriber,Contact,Newsletter,ServiceMagazineForm,ServiceSiteForm,Lohi

# Register your models here.
class SubscriberFilterAdmin(admin.ModelAdmin):
    list_filter = ('email', )
    list_display = ('email', 'subscribed_at')
    search_fields = ('email', 'subscribed_at')
    
class UserFilterAdmin(admin.ModelAdmin):
    list_filter = ('username', )
    list_display = ('username',)
    search_fields = ('username',)
    
class ContactFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name', 'email')
    search_fields = ('name', 'email')

class LohiFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name', 'message')
    search_fields = ('name', 'message')

class NewsletterFilterAdmin(admin.ModelAdmin):
    list_filter = ('subject', )
    list_display = ('subject', 'message')
    search_fields = ('subject', 'message')

class ServiceSiteFormFilterAdmin(admin.ModelAdmin):
    readonly_fields = ('service',)
    list_filter = ('name', )
    list_display = ('name', 'email')
    search_fields = ('name', 'email')

class ServiceMagazineFormFilterAdmin(admin.ModelAdmin):
    readonly_fields = ('service',)
    list_filter = ('name', )
    list_display = ('name', 'email')
    search_fields = ('name', 'email')

admin.site.register(User, UserFilterAdmin)
admin.site.register(Contact, ContactFilterAdmin)
admin.site.register(ServiceMagazineForm, ServiceMagazineFormFilterAdmin)
admin.site.register(ServiceSiteForm, ServiceSiteFormFilterAdmin)
admin.site.register(Newsletter, NewsletterFilterAdmin)
admin.site.register(Lohi, LohiFilterAdmin)
admin.site.register(Subscriber, SubscriberFilterAdmin)
