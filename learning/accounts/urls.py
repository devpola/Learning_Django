from django.contrib.auth.views import LoginView
from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login_form.html')),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/update/', views.profile_edit, name='profile_update'),
]