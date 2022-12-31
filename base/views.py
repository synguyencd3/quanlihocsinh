from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import  *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .form import *
from django.urls import reverse, reverse_lazy


# Create your views here.

def home(request):
    q = request.GET.get('q') if request.GET.get('q')!=None else ''
    context={}
    return render(request, 'base/home.html',context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method=='POST':
        username=request.POST.get('username').lower()
        password=request.POST.get('password')

        try:
            user=User.objects.get(username=username)
        except:
           messages.error(request, 'User not found')

        user = authenticate(request, username=username, password=password)

        if user is not None:
                login(request, user)
                return redirect('home')
        else:
            messages.error(request, 'Username or password does not exist')

    context= {}
    return render(request, 'base/login.html', context)

def registerPage(request):
    page='register'
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'Error occured')
    return render(request, 'base/signup.html', {'form':form, 'page':page})

def logoutUser(request):
    logout(request)
    return redirect('home')

def TiepnhanHS(request):
    form =HocSinhForm()
    gioitinh = 'male'
    if request.method=='POST':
        gender=request.POST.get('GIOITINH')
        print(gender)
        HOCSINH.objects.create(
            HOTEN=request.POST.get('HOTEN'),
            GIOITINH=gender,#request.POST.get('GIOITINH'),
            NGAYSINH= request.POST.get('NGAYSINH'),
            EMAIL= request.POST.get('EMAIL'),
        )
        return redirect('home')
    context = {'form':form}
    return render(request, 'base/TiepnhanHS.html', context)


def quanlidotuoi(request):
    age = Age.objects.all()
    context = {'age': age}
    return render(request, 'base/quanlidotuoi.html', context=context)



def capNhatTuoi(request, age_id):
    age = get_object_or_404(Age, id=age_id)
    form = ageForm(request.POST or None, instance=age)
    context = {
        'form': form,
        'subject_id': age_id,
        'page_title': 'capNhatTuoi'
    }
    if request.method == 'POST':
        if form.is_valid():
            year = form.cleaned_data.get('year')
            max_age = form.cleaned_data.get('max_age')
            min_age = form.cleaned_data.get('min_age')
            if max_age < min_age:
                messages.error(request, "Could Not Update")
                return render(request, "base/capNhatTuoi.html", context)
            else:
                try:
                    Year = Age.objects.get(id=age.id)
                    Year.year = year
                    Year.max_age = max_age
                    Year.min_age = min_age
                    Year.save()
                    messages.success(request, "Cập nhật thành công")
                    return redirect(reverse('quanlidotuoi'))
                except Exception as e:
                    messages.error(request, "Could Not Update " + str(e))
        else:
            messages.error(request, "Hãy điều đầy đủ vào ô thông tin !!!")
    else:
        return render(request, "base/capNhatTuoi.html", context)



def xoaTuoi(request, age_id):
    age = get_object_or_404(Age, id=age_id)
    age.delete()
    messages.success(request, "Age deleted successfully!")
    return redirect(reverse('quanlidotuoi'))



def themTuoi(request):
    form = ageForm(request.POST or None)
    context = {
        'form': form,
        'page_title': 'themTuoi'
    }
    if request.method == 'POST':
        if form.is_valid():
            year = form.cleaned_data.get('year')
            max_age = form.cleaned_data.get('max_age')
            min_age = form.cleaned_data.get('min_age')
            if max_age < min_age:
                messages.error(request, "Could Not Add")
                render(request, 'base/themTuoi.html', context)
            else:
                try:
                    Year = Age()
                    Year.year = year
                    Year.max_age = max_age
                    Year.min_age = min_age
                    Year.save()
                    messages.success(request, "Successfully Added")
                    return redirect(reverse('quanlidotuoi'))
                except:
                    messages.error(request, "Could Not Add")
        else:
            messages.error(request, "Lỗi định dạng")
    return render(request, 'base/themTuoi.html', context)

