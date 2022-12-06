from django.urls import path

from ticket.views import dash_board

urlpatterns = [
    path('', dash_board, name="dashboard"),
]
