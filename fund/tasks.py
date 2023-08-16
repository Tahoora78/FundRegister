# from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import *
from time import sleep
import requests


@shared_task()
def test_func(duration):
    for i in range(duration):
        print(i)
    return "Done"


@shared_task()
def save_data_info(data):
    fund = FundData(name=data['name'],
            regNo=data['regNo'],
            netAsset=data['netAsset'],
            cancelNav=data['cancelNav'],
            annualEfficiency=data['annualEfficiency'])
    fund.save()
    save_extra_info(data['regNo'])


@shared_task()
def save_extra_info(regNo):
    base_url = 'https://fund.fipiran.ir/api/v1/fund/getfund?regno='
    response = requests.get(base_url+str(regNo))
    data = response.json()

    fund = FundData.objects.get(regNo=regNo)

    fund.investmentManager = data['item']['investmentManager']
    fund.insInvNo = data['item']['insInvNo']
    fund.retInvNo = data['item']['retInvNo']
    fund.save()


@shared_task
def get_fund_info_by_regno(reg_no):
    data = FundData.objects.filter(regNo=reg_no).values()
    return data

@shared_task
def get_fund_info_by_name(sub_name):
    data = FundData.objects.filter(name__icontains=sub_name).values('regNo', 'name')
    return data