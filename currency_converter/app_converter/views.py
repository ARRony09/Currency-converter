from django.shortcuts import render
import json
import urllib.request
import requests
# Create your views here.

def index(request):
    if request.method=='POST':
        currency=request.POST['currency']
        currency2=request.POST['currency2']
        amount=request.POST['amount']
        source=urllib.request.urlopen('https://v6.exchangerate-api.com/v6/8d561674daf8e3e4f3537d77/pair/'+currency+'/'+currency2).read()
        list_of_data=json.loads(source)
        a=list_of_data['conversion_rate']
        total_amount=a*float(amount)
        data={
            'conversion_rate':str(list_of_data['conversion_rate']),
            'base_code':str(list_of_data['base_code']),
            'target_code':str(list_of_data['target_code']),
            'Amount':total_amount
        }
        """
        url='https://v6.exchangerate-api.com/v6/8d561674daf8e3e4f3537d77/pair/'+currency+'/'+currency2
        response=requests.get(url)
        data=response.json()
        
        list_of_data=json.loads(data)
        data={
            'conversion_rate':str(list_of_data['conversion_rate']),
        }
        """
        print(a)
    else:
        data={}


    return render(request,'index.html',context=data)