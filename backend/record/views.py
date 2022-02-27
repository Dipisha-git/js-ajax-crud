from multiprocessing.sharedctypes import Value
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from . models import Student
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def index(request):
    return render(request, 'index.html')


def api_data(request):
    sData = Student.objects.all().values()
    data = list(sData)
    return JsonResponse(data, safe=False)


@csrf_exempt
def add_student(request):
    if request.method == "POST":
        name = request.POST['name']
        address = request.POST['address']
        phone = request.POST['phone']
        Student.objects.create(name=name, address=address, phone=phone)
        res = {'success': 'Data was inserted'}
        return JsonResponse(res, safe=False)
    else:
        return redirect('index')


def delete_student(request, id):
    Student.objects.get(id=id).delete()
    res = {'success': 'Data was deleted'}
    return JsonResponse(res, safe=False)


@csrf_exempt
def edit_student(request, id):
    if request.method == 'POST':
        obj = Student.objects.get(id=id)
        obj.name = request.POST['name']
        obj.address = request.POST['address']
        obj.phone = request.POST['phone']
        obj.save()
        res = {'student': 'Data was updated'}
        return JsonResponse(res, safe=False)

    else:
        s = Student.objects.get(id=id)
        data = {'id': s.id, 'name': s.name,
                'address': s.address, 'phone': s.phone}

        return JsonResponse(data, safe=False)
