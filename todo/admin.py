from django.contrib import admin
from .models import *


class TaskAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Task._meta.fields]
    list_select_related = True

    class Meta:
        model = Task


admin.site.register(Task, TaskAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.fields]
    list_select_related = True

    class Meta:
        model = Category


admin.site.register(Category, CategoryAdmin)


# class ProfileAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in Profile._meta.fields]
#     list_select_related = True
#
#     class Meta:
#         model = Profile
#
#
# admin.site.register(Profile, ProfileAdmin)