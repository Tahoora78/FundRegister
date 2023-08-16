from rest_framework import serializers
from .models import FundData

class FundDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FundData
        fields = ['name', 'regNo', 'netAsset', 'cancelNav', 'annualEfficiency', 'investmentManager', 'insInvNo', 'retInvNo']