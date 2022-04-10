from django.contrib import admin
from levels.models import Level

class LevelAdmin(admin.ModelAdmin):
    # readonly_fields = ('forecast_date', 'create_date', 'value_date')
    list_display = ['forecast_date', 'create_date', 'value_date']
    search_fields = ['forecast_date', 'create_date', 'value_date']

admin.site.register(Level, LevelAdmin)
