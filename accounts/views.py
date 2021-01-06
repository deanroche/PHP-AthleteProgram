from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserRegistrationForm, UserLoginForm
from workouts.models import Workout
from contact.models import Contact
from datetime import date


# Views
def register(request):
    """
    Register User if all checks done in form validation are passed.
    If successful, return user to Index with notification of success &
    approval, else display error on register.html template.
    If User already logged in and URL injection used to navigate to
    register.html, redirect user to Index with error notification of same.
    :param request:
    :return:
    """
    if request.user.is_authenticated:
        messages.error(request, 'You are logged in already!')
        return redirect('index')
    elif request.method == 'POST':
        reg_form = UserRegistrationForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            messages.success(request, 'Please wait 24-hours before attempting '
                                      'to Login.')
            return redirect('index')
    else:
        reg_form = UserRegistrationForm()

    context = {
        'register_page': 'active',
        'form': reg_form
    }

    return render(request, 'accounts/register.html', context)


def user_login(request):
    """
    Log user in and redirect to Index page with success message.
    If user already logged in and attempt made to navigate to login page from
    URL injection display error message and redirect back to Index.
    :param request:
    :return:
    """
    if request.user.is_authenticated:
        messages.error(request, 'You are logged in already!')
        return redirect('index')
    elif request.method == 'POST':
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = authenticate(
                username=request.POST['username'],
                password=request.POST['password']
            )
            if user:
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'Successfully logged in.')
                    return redirect('index')
                else:
                    messages.error(request, 'Account not processed yet. Try '
                                            'again later!')
            else:
                messages.error(request, 'Invalid Login details!')
                return redirect('login')
    else:
        login_form = UserLoginForm()

    context = {
        'login_page': 'active',
        'form': login_form
    }
    return render(request, 'accounts/login.html', context)


def logout_view(request):
    """
    Logout User from current session & display success message of same.
    :param request:
    :return:
    """
    logout(request)
    messages.success(request, 'Thank you! You have successfully logged out.')
    return redirect('index')


def dashboard(request):
    """
    Navigate User to dashboard containing each day navigation for the PHP
    Athlete program.
    :param request:
    :return:
    """
    workouts = Workout.objects.filter(workout_date=date.today())
    unread_mail = Contact.objects.filter(read_status=False).count()

    context = {
        'dash_page': 'active',
        'workouts': workouts,
        'unread_count': unread_mail,
    }

    return render(request, 'accounts/dashboard.html', context)
