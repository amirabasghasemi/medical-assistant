from django.shortcuts import render


def ticket(request):
    return render(request, 'ticket/ticket.html')


def test(request):
    return render(request, 'ticket/test.html')


def experiment(request):
    return render(request, 'ticket/experiment.html')
