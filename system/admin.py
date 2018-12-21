from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.models import Permission

from system.models import Student, Group, Songs, Author


class StudentAdmin(ModelAdmin):
    list_display = ["name", "age", "group"]
    search_fields = ["name"]
    list_filter = ["group"]


admin.site.register(Group)
admin.site.register(Student, StudentAdmin)
admin.site.register(Songs)
admin.site.register(Author)
