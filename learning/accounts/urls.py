from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login_form.html')),
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/update/', views.profile_edit, name='profile_update'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
]