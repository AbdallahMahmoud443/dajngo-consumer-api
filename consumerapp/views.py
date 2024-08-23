from django.shortcuts import redirect, render
import requests

from consumerapp.forms import EmpolyeeForm
# Create your views here.





def Get_All_Employess(request):
    employessListUrl = "http://127.0.0.1:8000/api/viewsetsemployees/"
    empolyees =[]
    response =requests.get(f'{employessListUrl}')
    if response.status_code == 200:
        try:
            empolyees = response.json()
        except ValueError:
            empolyees = []
    else:
        empolyees = []
    return render(request,'drfconsumer/employeeList.html',{'empolyees':empolyees})


def Add_Employee(request):
    employessUrl = "http://127.0.0.1:8000/api/viewsetsemployees/"
    if request.method =="POST":
        form = EmpolyeeForm(request.POST)
        if form.is_valid():
            requests.post(employessUrl,data=form.data)
            return redirect('EmployeeListPage')
    else:
        form = EmpolyeeForm()
    
    return render(request,'drfconsumer/EmployeeInsert.html',{'form':form})


def Get_Employee(request,pk):
    employessUrl = f"http://127.0.0.1:8000/api/viewsetsemployees/{pk}/"
    response =requests.get(f'{employessUrl}')
    if response.status_code == 200:
        try:
            employee = response.json()
        except ValueError:
            employee = None
    else:
        employee = None
    
    form =EmpolyeeForm(employee,initial={
        #! Important to get Department && Country
        'Department':employee.get('Department'), # Department: 1 => IT
        'Country':employee.get('Country')
    })
 
    return render(request,'drfconsumer/EmployeeDetails.html',{'form':form})
    
def Delete_Employee(request,pk):
    
    employessUrl = f"http://127.0.0.1:8000/api/viewsetsemployees/{pk}/"
    response =requests.get(f'{employessUrl}')
    
    if response.status_code == 200:
        try:
            employee = response.json()
        except ValueError:
            employee = None
    else:
        employee = None
    
    form =EmpolyeeForm(employee,initial={
        #! Important to get Department && Country
        'Department':employee.get('Department'), # Department: 1 => IT
        'Country':employee.get('Country')
    })
    if request.method == "POST":
        response =requests.delete(f'{employessUrl}')
        return redirect('EmployeeListPage')
    
    return render(request,'drfconsumer/EmployeeDelete.html',{'form':form})

def Update_Employee(request,pk):
    
    employessUrl = f"http://127.0.0.1:8000/api/viewsetsemployees/{pk}/"
    response =requests.get(f'{employessUrl}')
    
    if response.status_code == 200:
        try:
            employee = response.json()
        except ValueError:
            employee = None
    else:
        employee = None
    
    form =EmpolyeeForm(employee,initial={
        #! Important to get Department && Country
        'Department':employee.get('Department'), # Department: 1 => IT
        'Country':employee.get('Country')
    })
    
    if request.method == "POST":
        form = EmpolyeeForm(request.POST)
        if form.is_valid():
            requests.put(f'{employessUrl}',data=form.data)
            return redirect('EmployeeListPage')
    return render(request,'drfconsumer/EmployeeUpdate.html',{'form':form})