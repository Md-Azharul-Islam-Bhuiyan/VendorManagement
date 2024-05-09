from django.urls import path
from .views import VendorListCreateAPIView, VendorRetrieveUpdateDestroyAPIView, VendorPerformanceView

urlpatterns = [
    path('', VendorListCreateAPIView.as_view(), name='vendor-list-create'),
    path('<int:pk>/', VendorRetrieveUpdateDestroyAPIView.as_view(), name='vendor-detail'),
    path('<int:pk>/performance/', VendorPerformanceView.as_view(), name='vendor-performance'),
]
