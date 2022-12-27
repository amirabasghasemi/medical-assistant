from django.contrib import admin
from ticket.models import TicketModel, SubTicketModel


class TicketAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_time'
    list_filter = ('status', )
    list_display = ('id', 'title', 'status')
    search_fields = ['title', 'status']


class SubTicketAdmin(admin.ModelAdmin):
    list_display = ('sender', 'text')

admin.site.register(SubTicketModel, SubTicketAdmin)
admin.site.register(TicketModel, TicketAdmin)
