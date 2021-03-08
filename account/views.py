from django.shortcuts import render, redirect
# from django.contrib.auth import get_user_model
# from .models import BlogPost

from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def register(response):
    if response.method == 'POST': 
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect('/')
    else:
        form = RegisterForm()
    return render(response, 'account/register.html', {'form': form})
# def register(request):
#     return render(request, 'account/register.html')

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            login(request, user)
            form.save()
        return redirect("/")
    else:
        form = LoginForm()
        
            # if user == None:
            #     request.session["invalid_user"] == 1
            #     return render(request,'account/login_view.html', {'form':form})
    return render(request, 'account/login_view.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/login')
# def home(request):
#     user_model = get_user_model()
#     all_users = user_model.objects.all()
#     return render(request, 'account/home.html', {'all_users': all_users})


# def create_new_user(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         name = request.POST['name']
#         password = request.POST['password']
#         blog_title =request.POST['blog_title']
#         user_model = get_user_model()
       
#         user_object = user_model.objects.create_user(email=email, name=name)
#         user_object.set_password(password)
#         user_object.blogpost.title = blog_title
#         user_object.save()
#         return redirect('home')
#     else:
#         return render(request, 'create_new_user.html')