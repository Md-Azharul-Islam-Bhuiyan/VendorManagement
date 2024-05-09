from django.urls import path
from .views import PurchaseOrderListCreateView, PurchaseOrderRetrieveUpdateDestroyAPIView, AcknowledgePurchaseOrder


urlpatterns = [
    path('', PurchaseOrderListCreateView.as_view(), name='PurchaseOrder_list_create'),
    path('<int:pk>/', PurchaseOrderRetrieveUpdateDestroyAPIView.as_view(), name="PurchaseOrder-detail"),
    path('<int:pk>/acknowledge/', AcknowledgePurchaseOrder.as_view(), name='acknowledge-purchase-order')
]
