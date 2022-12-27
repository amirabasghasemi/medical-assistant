from django.urls import path

from ticket.views import tickets

urlpatterns = [
    path('', tickets, name="tickets"),
]
