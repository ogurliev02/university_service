from django.contrib import admin

from adm.models import (
    Profile,
    Category,
    Project,
    Mark,
    University,
)


class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = [field.name for field in model._meta.fields if field.name != "id"]


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = [field.name for field in model._meta.fields if field.name != "id"]


class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = [field.name for field in model._meta.fields if field.name != "id"]


class MarkAdmin(admin.ModelAdmin):
    model = Mark
    list_display = [field.name for field in model._meta.fields if field.name != "id"]


class UniversityAdmin(admin.ModelAdmin):
    model = University
    list_display = [field.name for field in model._meta.fields if field.name != "id"]


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Mark, MarkAdmin)
admin.site.register(University, UniversityAdmin)