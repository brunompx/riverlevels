from django.contrib import admin
from levels.models import Level

class LevelAdmin(admin.ModelAdmin):
    pass

admin.site.register(Level, LevelAdmin)
