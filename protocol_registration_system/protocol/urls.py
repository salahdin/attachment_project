from django.urls import path
from .import views

app_name="protocol"
urlpatterns = [
    path('apply',views.apply,name='apply'),
    ]