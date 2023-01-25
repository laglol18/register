from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from .forms import CreateUserForm
def home(request):
    return render(request, 'app/home.html')

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'app/register.html', context)

def loginPage(request):
    form = UserCreationForm()
    context = {'form': form}
    return render(request, 'app/login.html', context)
