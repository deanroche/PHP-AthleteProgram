from django.shortcuts import render
from contact.models import Contact


# Create your views here.
def index(request):
    unread_mail = Contact.objects.filter(read_status=False).count()

    # context to produce active state of current page in nav-item to user.
    context = {
        'home_page': 'active',
        'unread_count': unread_mail,
    }

    return render(request, 'pages/index.html', context)


def accessibility(request):
    unread_mail = Contact.objects.filter(read_status=False).count()
    context = {
        'unread_count': unread_mail,
    }
    return render(request, 'pages/accessibility.html', context)


def privacy(request):
    unread_mail = Contact.objects.filter(read_status=False).count()
    context = {
        'unread_count': unread_mail,
    }
    return render(request, 'pages/privacy.html', context)


def admin(request):
    return render(request, 'admin')
