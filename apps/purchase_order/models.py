from django.db import models
from apps.vendor.models import VendorModel
from apps.purchase_order.constants import STATUS_TYPE


class Purchase_OrderModel(models.Model):

    po_number = models.CharField(max_length=100, unique=True)
    vendor = models.ForeignKey(VendorModel, on_delete=models.CASCADE, null=True, blank=True)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=100, choices=STATUS_TYPE, default="Pending")
    quality_rating = models.FloatField(default=0.0)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField()

    def __str__(self):
        return self.po_number