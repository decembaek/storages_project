from django.contrib import admin

from .models import Excel


# Register your models here.
@admin.register(Excel)
class ExcelAdmin(admin.ModelAdmin):
    pass
