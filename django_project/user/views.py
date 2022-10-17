from django.shortcuts import render,redirect
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'Welcome {name} your registration has been created! You can now log in.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    context = {'form':form}
    return render(request, 'user/register.html', context)


@login_required
def profile(request):
    return render(request, 'user/profile.html')
