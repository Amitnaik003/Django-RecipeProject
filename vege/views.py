from django.shortcuts import render, get_object_or_404, redirect
from .models import Receipe
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def receipes(request):
    if request.method == "POST":
        receipe_name = request.POST.get('receipe_name')
        receipe_discription = request.POST.get('receipe_discription')
        receipe_image = request.FILES.get('receipe_image')
        
        Receipe.objects.create(
            receipe_name=receipe_name,
            receipe_discription=receipe_discription,
            receipe_image=receipe_image,
        )
        return redirect('receipes')

    queryset = Receipe.objects.all()
    context = {
        'receipes': queryset,
    }
    return render(request, 'receipes.html', context)

def delete_receipe(request, id):
    receipe = get_object_or_404(Receipe, id=id)
    receipe.delete()
    return redirect('receipes')

def update_receipe(request, id):
    receipe = get_object_or_404(Receipe, id=id)
    if request.method == "POST":
        receipe_name = request.POST.get('receipe_name')
        receipe_discription = request.POST.get('receipe_discription')
        receipe_image = request.FILES.get('receipe_image')

        receipe.receipe_name = receipe_name
        receipe.receipe_discription = receipe_discription
        if receipe_image:
            receipe.receipe_image = receipe_image
        receipe.save()
        return redirect('receipes')

    context = {"receipe": receipe}
    return render(request, 'update_receipes.html', context)

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.info(request, 'Login successful')
            return redirect('receipes')
        else:
            messages.info(request, 'Invalid name or password')
            return redirect('login_page')

    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect('login_page')

def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username already exists')
            return redirect('register_page')

        user = User(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        user.set_password(password)
        user.save()
        messages.info(request, 'Account created successfully')
        return redirect('login_page')

    return render(request, 'register.html')


