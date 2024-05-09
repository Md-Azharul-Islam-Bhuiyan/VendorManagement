from rest_framework import serializers
from .models import HistoricalPerformanceModel


class HistoricalPerformanceSerializers(serializers.ModelSerializer):
    model=HistoricalPerformanceModel
    fields="__all__"