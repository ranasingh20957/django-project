from django.contrib import admin
from SMS.models import student

# Register your models here.

#admin.site.register(student)


@admin.register(student)
class studentAdmin(admin.ModelAdmin):
    list_display=['name','mobileno','address','created_date']

