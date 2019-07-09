from django.urls import path
from .import views

app_name="protocol"
urlpatterns = [
    path('apply', views.apply, name='apply'),
    path('list', views.ProtocolRequestListView.as_view(), name='protocol-request-list',)
    ]