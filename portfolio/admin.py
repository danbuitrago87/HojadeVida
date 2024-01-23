from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):       #se define una clase ProjectAdmin que hereda de admin
    readonly_fields=('created','updated')   #campos de solo lectura

admin.site.register(Project, ProjectAdmin)