from django.urls import path

from ticket.views import ticket, recent_tickets

urlpatterns = [
    path('', ticket, name="ticket"),
    path('recent/', recent_tickets, name="recent-tickets"),
    # path('#recent-tickets/<int:ticket_id>', ticket_by_id, name='ticket_by_id'),
]
