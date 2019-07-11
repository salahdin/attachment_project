from django.urls import path
from .import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('signup/', views.signup, name="signup"),
    ]