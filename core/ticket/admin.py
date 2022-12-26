from django.contrib import admin
from ticket.models import TicketModel


class TicketAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_time'
    list_filter = ('status', )
    list_display = ('id', 'title', 'status')
    search_fields = ['title', 'status']


admin.site.register(TicketModel, TicketAdmin)
