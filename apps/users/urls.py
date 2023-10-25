from django.urls import path
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
#my imports
from apps.users import views,resset_password

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.user_login, name="login"),
    path('profile/<int:id>/', views.profile, name="profile"),
    path("logout/", LogoutView.as_view(next_page = "index"), name = "logout"),
    
    # reset password
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='users/forgot-password.html', extra_context={'setting': views.get_latest_settings}), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/forgot-password_done.html', extra_context={'setting': views.get_latest_settings}), name='password_reset_done'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='users/forgot-password_complete.html', extra_context={'setting': views.get_latest_settings}), name='password_reset_complete'),
    path('reset/<uidb64>/<token>/', resset_password.custom_password_reset_confirm, name='password_reset_confirm'),
    
]