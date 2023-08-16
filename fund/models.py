from django.db import models

    
class FundData(models.Model):
    name = models.CharField(max_length=200)
    regNo = models.IntegerField(primary_key=True)
    netAsset = models.IntegerField(null=True)
    cancelNav = models.FloatField(null=True)
    annualEfficiency = models.FloatField(null=True)
    investmentManager = models.CharField(max_length=200, null=True)
    insInvNo = models.IntegerField(null=True)
    retInvNo = models.IntegerField(null=True)

    