from django.urls import path

from ticket.views import ticket, test,experiment

urlpatterns = [
    path('', ticket, name="ticket"),
    path('#0', test, name="test"),
    path('#', experiment, name="experiment"),
]
