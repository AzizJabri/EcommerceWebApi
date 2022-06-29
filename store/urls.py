from django.urls import path
from .views import *

urlpatterns = [
    path('stores/', StoreListView.as_view(), name='store-list'),
    path('store/<int:pk>/', StoreDetailView.as_view(), name='store-detail'),
]
