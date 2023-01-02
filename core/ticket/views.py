from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404

from ticket.forms import TicketForm, SubTicketForm
from ticket.models import TicketModel, SubTicketModel


def ticket_conversation(request, pk):
    ticket = get_object_or_404(TicketModel, pk=pk)
    if ticket.created_by != request.user:
        return Http404
    if request.method == 'POST':
        form = SubTicketForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.parent = ticket
            instance.sender = request.user
            ticket.change_unread(request.user)
            form.save()
            return redirect('ticket-conversation', pk)
        return redirect('ticket-conversation', pk)
    else:
        form = SubTicketForm()
        conversations = SubTicketModel.objects.filter(parent=ticket).order_by('-created_time')
        return render(request, 'dashboard/conversation.html', {
            'form': form, 'conversations': conversations, 'ticket': ticket
        })


def tickets(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.created_by = request.user
            instance.change_unread(request.user)
            form.save()
        return redirect('tickets')
    else:
        form = TicketForm()
        ticket = TicketModel.objects.filter(created_by=request.user).order_by('-created_time')
        paginator = Paginator(ticket, 2)
        page_number = request.GET.get('page', 1)

        all_tickets = paginator.get_page(page_number)
        return render(request, 'dashboard/ticket.html', {'all_tickets': all_tickets, 'form': form})

