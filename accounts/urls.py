from django.urls import path
from .views import AccountCreateView, AccountDetailView

urlpatterns = [
   path('new/', AccountCreateView.as_view(), name='account_new'), 
   path('detail/', AccountDetailView.as_view(), name='account_detail'),
    ]
