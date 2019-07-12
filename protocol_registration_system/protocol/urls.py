from django.urls import path
from .import views

app_name="protocol"
urlpatterns = [
    path('apply/', views.apply, name='apply'),
    path('list/', views.ProtocolRequestListView.as_view(), name='protocol-request-list',),
    path('detail/<int:id>', views.ProtocolRequestDetailView.as_view(), name='protocol-request-detail',),
    path('approve/<int:id>', views.approve_request, name='approve'),
    path('reject/<int:id>', views.reject_request, name='reject'),

]