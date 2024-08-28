from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard-index')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout

@login_required
def user_list(request):
    if not request.user.is_superuser:
        return redirect('dashboard-index')
    users = User.objects.all()
    return render(request, 'accounts/user_list.html', {'users': users})

@login_required
def password_reset(request, user_id):
    if not request.user.is_superuser:
        return redirect('dashboard-index')
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = SetPasswordForm(user)
    return render(request, 'accounts/password_reset.html', {'form': form, 'user': user})

