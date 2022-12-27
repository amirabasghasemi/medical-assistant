from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from ticket.forms import TicketForm
from ticket.models import TicketModel


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
        ticket = TicketModel.objects.order_by('-created_time')
        paginator = Paginator(ticket, 2)
        page_number = request.GET.get('page', 1)

        all_tickets = paginator.get_page(page_number)
        return render(request, 'dashboard/ticket.html', {'all_tickets': all_tickets, 'form': form})


# def ticket_by_id(request, ticket_id):
#     ticket = TicketModel.objects.get(pk=ticket_id)
#     return render(request, 'ticket/ticket.html', {'ticket': ticket})

