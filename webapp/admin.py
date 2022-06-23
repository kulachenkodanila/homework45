from django.contrib import admin

from webapp.models import Work


class WorkAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'status', 'd_date']
    list_filter = ['status', 'd_date']
    search_fields = ['description']
    fields = ['id', 'description', 'status', 'd_date']
    readonly_fields = ['status']


admin.site.register(Work, WorkAdmin)
