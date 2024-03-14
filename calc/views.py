from django.shortcuts import render
from django.http import HttpResponse
from .models import userProp

def home(request):
    content = {'name': "Deena"}
    obj = userProp.objects.filter(name='python')
    print(obj)
    return render(request, 'home.html', content)


def result(request):
    res_num = 0
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    res_num = num1 + num2
    operation = request.POST['operation']

    if operation =='add':
        res_num = num1+num2
    elif operation == 'sub':
        res_num = num1 - num2
    elif operation == 'div':
        res_num = num1/num2
    else:
        res_num = num1 * num2

    return render(request, 'result.html', {'result': res_num})