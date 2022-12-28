from django.contrib import admin

from django.contrib.admin import register

from analyze.models import DiabetesModel


@register(DiabetesModel)
class DiabetesAdmin(admin.ModelAdmin):
    list_display = ['user', 'result']

