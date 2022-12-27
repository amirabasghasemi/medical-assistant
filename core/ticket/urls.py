from django.urls import path

from ticket.views import tickets, ticket_conversation

urlpatterns = [
    path('', tickets, name="tickets"),
    path('<int:pk>/', ticket_conversation, name="ticket-conversation"),
]
