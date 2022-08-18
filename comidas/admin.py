from django.contrib import admin
from.models import Banquete

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('create', 'updated' )


admin.site.register(Banquete, ProjectAdmin)
