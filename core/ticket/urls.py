from django.urls import path

from ticket.views import ticket, recent_tickets, test, experiment

urlpatterns = [
    path('tickets', ticket, name="ticket"),
    path('tests', test, name="test"),
    path('experiments', experiment, name="experiment"),
    path('tickets/recent', recent_tickets, name="recent-tickets"),
    # path('#recent-tickets/<int:ticket_id>', ticket_by_id, name='ticket_by_id'),
]
