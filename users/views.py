from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # messages.success(request, f'Your account has been created! You can now log in')
            return redirect('users:login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/signup.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST)
        p_form = ProfileUpdateForm(request.POST)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            username = u_form.cleaned_data.get('username')
            messages.success(request, f'Your profile has been updated!')
            return redirect('/')
    else:
        u_form = UserUpdateForm(request.POST)
        p_form = ProfileUpdateForm(request.POST)
    return render(request, 'users/profile.html', {'u_form': u_form,
                                                  'p_form': p_form})

