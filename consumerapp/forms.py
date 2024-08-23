# you should create form form scratch because you don't have model in database 
from django import forms
import requests


def Get_Departments_List():
    response = requests.get('http://127.0.0.1:8000/departmentlist/')
    if response.status_code == 200:
        return response.json()
    
def Get_country_List():
    response = requests.get('http://127.0.0.1:8000/countrylist/')
    if response.status_code == 200:
        return response.json()
   
# used forms.Form => because you build model form scratch
class EmpolyeeForm(forms.Form):
    FirstName = forms.CharField(max_length=30)
    LastName  = forms.CharField(max_length=30)
    TitleName = forms.CharField(max_length=30)
    HasPassport = forms.BooleanField()
    Salary = forms.IntegerField()
    HireDate = forms.DateField()
    Notes = forms.CharField(max_length=200)
    Email = forms.EmailField(max_length=50)
    PhoneNumber = forms.CharField(max_length=20)
    Department = forms.ChoiceField(choices=Get_Departments_List())
    Country= forms.ChoiceField(choices=Get_country_List())
    
    class Meta:
        fields =[
            'FirstName',
            'LastName',
            'TitleName',
            'HasPassport',
            'Salary',
            'HireDate',
            'Notes',
            'Email',
            'PhoneNumber',
            'Department',
            'Country'
        ]
        widgets ={
            'HireDate':forms.widgets.DateInput(attrs={'type':'date'}),
        }