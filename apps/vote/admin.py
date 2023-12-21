from django.contrib import admin
from .models import Nomination, Option, Vote,Advert,VotingInfo

####################################################################################################
class AdvertFilterAdmin(admin.ModelAdmin):
    verbose_name_plural = 'Новости'
    list_filter = ('url', )
    list_display = ('url', 'image')
    search_fields = ('url', 'image')


class VotingInfoFilterAdmin(admin.ModelAdmin):
    list_filter = ('title','descriptions', 'end_time')
    list_display = ('title', 'descriptions', 'end_time')
    search_fields = ('title', 'descriptions', 'end_time')

admin.site.register(VotingInfo,VotingInfoFilterAdmin)
admin.site.register(Advert,AdvertFilterAdmin)
####################################################################################################

class OptionInline(admin.TabularInline):
    model = Option
    extra = 1

class VoteInline(admin.TabularInline):
    model = Vote
    fields = ['user', 'option', 'date_voted']
    readonly_fields = ['user', 'option', 'date_voted']
    extra = 0

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Если мы в контексте конкретной номинации, фильтруем голоса по этой номинации
        if request.resolver_match.kwargs.get('object_id'):
            nomination_id = request.resolver_match.kwargs['object_id']
            qs = qs.filter(nomination_id=nomination_id)
        return qs

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "option":
            if request.resolver_match.kwargs.get('object_id'):
                nomination_id = request.resolver_match.kwargs['object_id']
                kwargs["queryset"] = Option.objects.filter(nomination_id=nomination_id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Nomination)
class NominationAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'end_date', 'is_published', 'order']
    inlines = [OptionInline, VoteInline]

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['user', 'option', 'nomination', 'date_voted']
    list_filter = ['nomination', 'user', 'option']
    date_hierarchy = 'date_voted'
    fieldsets = (
        ('Номинация', {
            'fields': ('nomination',)
        }),
        ('Дополнительная информация', {
            'fields': ('option', 'user', 'date_voted')
        }),
    )
    readonly_fields = ['nomination', 'option', 'user', 'date_voted']
