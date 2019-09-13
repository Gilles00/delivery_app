from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from users.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission


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
def profile(request, pk):
    user = get_object_or_404(User,pk=pk)
    user_profile = get_object_or_404(Profile,user_id=request.user.id)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=user_profile)
        if u_form.is_valid() and p_form.is_valid():
            user = u_form.save()
            user_profile = p_form.save()
            permission = Permission.objects.get(name='Can Add Kitchen')
            if user_profile.is_Provider == 1:
                user.user_permissions.add(permission)
            else:
                user.user_permissions.remove(permission)
            messages.success(request, f'Your profile has been updated!')
            return redirect('users:profile', pk=user.id,)
    else:
        u_form = UserUpdateForm(instance=user)
        p_form = ProfileUpdateForm(instance=user_profile)
    return render(request, 'users/profile.html', {'u_form': u_form,
                                                  'p_form': p_form,
                                                  'profile':user_profile})

