from django.contrib import admin
from project_management.models import Organization, Department, Team, Project, Task


# Register your models here.
@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    pass


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass
