from django.shortcuts import render
from ticket.forms import TicketForm


def dash_board(request):
    TickForm = TicketForm()
    return render(request, 'ticket/ticket.html', {'TickForm': TickForm})
