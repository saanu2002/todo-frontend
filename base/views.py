from django.shortcuts import render, redirect
import requests
import json

BASE_URL = 'https://todo-backend-42le.onrender.com'

# Create your views here.
def home(request):
    url = f'{BASE_URL}/api/tasks/'

    resp = requests.get(url=url)

    print("Status Code:", resp.status_code)
    print("Response Text:")
    print(resp.text)

    py_data = resp.json()

    return render(request, 'home.html', {'data': py_data})

def add(request):
    url = f'{BASE_URL}/api/tasks/'
    if request.method == 'POST':
        title=request.POST['title']
        desc=request.POST['desc']
        print(title,desc)
        py_data = {
            'title':title,
            'desc':desc
        }
        print(py_data)
        print(type(py_data))
        json_data = json.dumps(py_data)
        print(json_data)
        print(type(json_data))
        resp=requests.post(
            url=url,
            data=json_data
            )
        print(resp)#<Response [403]> #<Response [200]>
        print(resp.json())
        return redirect('home')
    return render(request,'add.html')

def complete(request):
    return render(request,'complete.html')

def trash(request):
    return render(request,'trash.html')

def about(request):
    return render(request,'about.html')

def update(request,id):
    print(id)
    url = f'{BASE_URL}/api/task/{id}'
    resp=requests.get(url=url)
    print(resp)
    py_data=resp.json()
    print(py_data)
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        py_data = {
            'title':title,
            'desc':desc
        }
        json_data=json.dumps(py_data)
        print(json_data)
        resp=requests.put(url=url,data=json_data)
        print(resp.json())
        return redirect('home')
    return render(request,'update.html',{'data':py_data})

def delete_(request,id):
    url = f'{BASE_URL}/api/task/{id}'
    resp=requests.delete(url=url)
    return redirect('home')

'''
loads and dumps
json.dumps()
convert the python data into JSON string

json.loads()
convert the JSON string into python data
'''