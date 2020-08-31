from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'pages/index.html')


def accessibility(request):
    return render(request, 'pages/accessibility.html')


def privacy(request):
    return render(request, 'pages/privacy.html')
