from django.shortcuts import render
from DBModelApp.models import Employee,Company
# Create your views here.
def empdata(request):
    emplist=Employee.objects.all()
    dict1={'emplist':emplist}
    return render(request,'DBModelApp/emp.html',context=dict1)

def compdata(request):
    comp=Company.objects.all()
    dict1={'comp':comp}
    return render(request,'DBModelApp/comp.html',context=dict1)