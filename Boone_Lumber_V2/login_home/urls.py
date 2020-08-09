from django.urls import path

from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name="logout"),

    path('reset_password/', auth_views.PasswordResetView.as_view(
            template_name="login_home/reset_password.html",
            email_template_name='login_home/password_reset_email.html',
            subject_template_name='login_home/password_reset_subject.txt'),
         name='password_reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="login_home/reset_password_sent.html"),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="login_home/password_reset_form.html"),
         name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="login_home/password_reset_done.html"),
         name='password_reset_complete'),


]