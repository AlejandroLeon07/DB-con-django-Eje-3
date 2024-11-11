from django.contrib import admin
from .models import curso

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("fecha_creacion", )

# Register your models here.
admin.site.register(curso, TaskAdmin)

