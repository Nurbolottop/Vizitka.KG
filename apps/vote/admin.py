from django.contrib import admin
from .models import Nomination, Option

class OptionInline(admin.TabularInline):
    model = Option
    extra = 1  # Количество пустых форм для новых вариантов

@admin.register(Nomination)
class NominationAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'end_date', 'is_published', 'order']
    ordering = ['order']
    search_fields = ['name']
    inlines = [OptionInline]

# Если вам не нужен отдельный admin для Option, просто не регистрируйте его.
# Если он нужен, оставьте регистрацию без использования декоратора:
# admin.site.register(Option, OptionAdmin)
