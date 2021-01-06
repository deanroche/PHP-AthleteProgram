from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from .forms import ContactForm


# Create your views here.
def contact(request):
    """
    Contact Template rendered along with Contact Form.
    If user authenticated, contact_name field auto-populated with User name,
    else User is prompted to enter name.
    Form on Submit saved in DB for Admin view.
    """
    unread_mail = Contact.objects.filter(read_status=False).count()

    if request.method == 'POST':
        if request.user.is_authenticated:
            create_contact_form = Contact(
                contact_title=request.POST.get('contact_title'),
                contact_body=request.POST.get('contact_body'),
                contact_name=request.user,
                contact_email=request.POST.get('contact_email'),
            )
            create_contact_form.save()
        else:
            create_contact_form = Contact(
                contact_title=request.POST.get('contact_title'),
                contact_body=request.POST.get('contact_body'),
                contact_email=request.POST.get('contact_email'),
            )
            create_contact_form.save()

        messages.success(request, 'Thanks for getting in touch, we will '
                                  'respond as soon as we can.')
        return redirect('index')

    context = {
        'form': ContactForm,
        'unread_count': unread_mail
    }

    return render(request, 'contact/contact.html', context)
