from django.contrib import admin
from  .models import User,Subscriber

# Register your models here.
class SubscriberFilterAdmin(admin.ModelAdmin):
    list_filter = ('email', )
    list_display = ('email', 'subscribed_at')
    search_fields = ('email', 'subscribed_at')
    
    
admin.site.register(User)
admin.site.register(Subscriber, SubscriberFilterAdmin)
