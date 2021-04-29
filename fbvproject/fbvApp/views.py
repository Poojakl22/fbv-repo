from django.shortcuts import render
from fbvApp.models import Employee
# Create your views here.
def display(request):
      e=Employee.objects.all()
      d={'emp':e}
      return render(request,'myApp/index.html',d)