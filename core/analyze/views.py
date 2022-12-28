from django.shortcuts import render


def test(request):
    if request.method == "POST":
        pass
    else:
        return render(request, 'dashboard/test.html')

def results(request):
    pass



