from django.http import HttpResponse
from django.shortcuts import render
from .tasks import *
from .models import *
import requests
from django.http import JsonResponse
from .models import FundData
from rest_framework.decorators import api_view


def test(request):
    test_func(6)
    return HttpResponse('Done') 

@api_view(['POST'])
def save_fund_info(request):
    response = requests.get('https://fund.fipiran.ir/api/v1/fund/fundcompare')
    data = response.json()  
    for item in data['items']:
        result = dict()
        result['name'] = item['name']
        result['regNo'] = int(item['regNo'])
        result['netAsset'] = item['netAsset']
        result['cancelNav'] = item['cancelNav']
        result['annualEfficiency'] = item['annualEfficiency']
        save_data_info(result)
    return HttpResponse('All data saved')
        
@api_view(['GET'])
def show_fund_info_by_regno(request, reg_no):    
    return JsonResponse({'data':get_fund_info_by_regno(reg_no)}, safe=False)

@api_view(['GET'])
def show_fund_info_by_name(request, name):
    return JsonResponse({'data':get_fund_info_by_name(name)}, safe=False)