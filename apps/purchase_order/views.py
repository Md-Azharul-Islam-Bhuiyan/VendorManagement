from apps.purchase_order.models import Purchase_OrderModel
from .serializers import Purchase_OrderSerializers, AcknowledgementPurchaseOrder
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class PurchaseOrderListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Purchase_OrderModel.objects.all()
    serializer_class = Purchase_OrderSerializers


class PurchaseOrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Purchase_OrderModel.objects.all()
    serializer_class = Purchase_OrderSerializers            
    

class AcknowledgePurchaseOrder(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Purchase_OrderModel.objects.all()
    serializer_class = AcknowledgementPurchaseOrder

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)