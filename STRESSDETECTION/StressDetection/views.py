from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import UserRegistrationForm
# from django.shortcuts import redirect


def index(request):
    return render(request, 'index.html', {})

def logout(request):
    return render(request, 'index.html', {})

def UserLogin(request):
    return render(request, 'UserLogin.html', {})

def AdminLogin(request):
    return render(request, 'AdminLogin.html', {})


# def UserRegister(request):
#     form = UserRegistrationForm()
#     return render(request, 'UserRegistrations.html', {'form': form})

def UserRegister(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()   # 🔥 THIS SAVES USER TO DATABASE
            messages.success(request, "Registration successful. Please login.")
            return redirect('UserLogin')
        else:
            messages.error(request, "Registration failed. Please check details.")
    else:
        form = UserRegistrationForm()

    return render(request, 'UserRegistrations.html', {'form': form})

