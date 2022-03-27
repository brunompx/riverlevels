from django.contrib import admin
from levels.models import Level

class LevelAdmin(admin.ModelAdmin):
    readonly_fields = ('forecast_date', 'create_date', 'value_date')
    pass

admin.site.register(Level, LevelAdmin)
