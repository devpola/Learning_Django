from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, UpdateView, CreateView

from .forms import ProfileForm
from .models import Profile

User = get_user_model()


# @login_required
# def profile(request):
#     return render(request, 'accounts/profile.html')
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm

@login_required()
def profile_edit(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = None

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect(profile)
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'accounts/profile_form.html', {
        'form': form
    })

def signup(request):
    pass

class SignUpView(CreateView):
    model = User
    form_class = UserCreationForm   # username, password1, password2(confirmation)
    success_url = settings.LOGIN_URL
    template_name = 'accounts/signup_form.html'

def logout(request):
    pass