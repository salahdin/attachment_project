from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login
# Create your views here.
def signup(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('protocol:protocol-request-list')
    else:
        form = UserCreationForm
    return render(request, 'accounts/signup.html', {'form': form})


def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('protocol:protocol-request-list')

    else:
        form = AuthenticationForm
    return render(request, 'accounts/login.html', {'form': form})

