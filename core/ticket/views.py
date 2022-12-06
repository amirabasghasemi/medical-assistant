from django.shortcuts import render


def dash_board(request):
    return render(request, 'ticket/index.html')
