from django.contrib import admin
from  .models import User,Subscriber,Contact,Newsletter

# Register your models here.
class SubscriberFilterAdmin(admin.ModelAdmin):
    list_filter = ('email', )
    list_display = ('email', 'subscribed_at')
    search_fields = ('email', 'subscribed_at')
    
class UserFilterAdmin(admin.ModelAdmin):
    list_filter = ('username', )
    list_display = ('username', 'email')
    search_fields = ('username', 'email')
    
class ContactFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name', 'email')
    search_fields = ('name', 'email')

class NewsletterFilterAdmin(admin.ModelAdmin):
    list_filter = ('subject', )
    list_display = ('subject', 'message')
    search_fields = ('subject', 'message')


admin.site.register(User, UserFilterAdmin)
admin.site.register(Contact, ContactFilterAdmin)
admin.site.register(Newsletter, NewsletterFilterAdmin)
admin.site.register(Subscriber, SubscriberFilterAdmin)
