from django.contrib import admin
from .models import Project, Technology


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'current', 'type')
    list_filter = ('current', 'type')
    filter_horizontal = ('technologies',)
    
    
# Register your models here.
admin.site.register(Project, ProjectAdmin)
admin.site.register(Technology)