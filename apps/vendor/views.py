from apps.vendor.models import VendorModel
from apps.purchase_order.models import Purchase_OrderModel 
from apps.vendor.serializers import VendorSerializer
from django.db.models import Avg, F
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class VendorListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = VendorModel.objects.all()
    serializer_class = VendorSerializer


class VendorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = VendorModel.objects.all()
    serializer_class = VendorSerializer


class VendorPerformanceView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = VendorModel.objects.all()
    serializer_class = VendorSerializer

    def retrieve(self, request, *args, **kwargs):
        vendor = self.get_object()
        completed_pos = Purchase_OrderModel.objects.filter(status='Completed')
        total_completed_pos = completed_pos.count()
        # print(total_completed_pos)
        on_time_delivery_rate = completed_pos.filter(delivery_date__lte=F('acknowledgment_date')).count() / total_completed_pos if total_completed_pos > 0 else 0
        quality_rating_avg = completed_pos.exclude(quality_rating=None).aggregate(avg_quality_rating=Avg('quality_rating'))['avg_quality_rating'] or 0

        avg_response_time = completed_pos.exclude(acknowledgment_date=None).aggregate(avg_response_time=Avg(F('acknowledgment_date') - F('issue_date')))['avg_response_time'] or 0

        fulfillment_rate = completed_pos.filter(status='Completed').count() / Purchase_OrderModel.objects.filter(vendor=vendor).count() if Purchase_OrderModel.objects.filter(vendor=vendor).count() > 0 else 0
        
        performance_data = {
            'on_time_delivery_rate': on_time_delivery_rate,
            'quality_rating_avg': quality_rating_avg,
            'average_response_time': avg_response_time / 60,  # Convert to minutes
            'fulfillment_rate': fulfillment_rate
        }

        return Response(performance_data, status=status.HTTP_200_OK)
