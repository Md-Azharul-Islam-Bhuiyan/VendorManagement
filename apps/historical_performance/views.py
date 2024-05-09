from .models import HistoricalPerformanceModel
from .serializers import HistoricalPerformanceSerializers
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class PerformanceEvaluation(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = HistoricalPerformanceModel.objects.all()
    serializer_class = HistoricalPerformanceSerializers
