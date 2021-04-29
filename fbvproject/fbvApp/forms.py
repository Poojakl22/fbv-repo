from django import forms
from fbvApp.models import Employee
class EmployeeForm(forms.ModelFrom):
       class Meta:
           model=Employee
           fields='__all__'
