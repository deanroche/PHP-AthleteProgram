from django.shortcuts import render


# Create your views here.
def index(request):
    # context to produce active state of current page in nav-item to user.
    context = {
        'home_page': 'active'
    }

    return render(request, 'pages/index.html', context)


def accessibility(request):
    return render(request, 'pages/accessibility.html')


def privacy(request):
    return render(request, 'pages/privacy.html')


def admin(request):
    return render(request, 'admin')
