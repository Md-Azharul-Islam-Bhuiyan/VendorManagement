from .models import Purchase_OrderModel
from rest_framework import serializers


class Purchase_OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Purchase_OrderModel
        fields = '__all__'


class AcknowledgementPurchaseOrder(serializers.ModelSerializer):
    class Meta:
        model = Purchase_OrderModel
        fields = ['acknowledgment_date']