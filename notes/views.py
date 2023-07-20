from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from django.views.generic.list import ListView
from django.core.exceptions import ValidationError
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


# Create your views here.
def index(request):
    return render(request, 'notes/login.html')


def register(request):
    if request.method == 'POST':
        a = request.POST.get('name')
        b = request.POST.get('username')
        c = request.POST.get('email')
        d = request.POST.get('password')
        e = request.POST.get('confirmpassword')
        if d == e:
            if Customer.objects.filter(username=b).exists():
                messages.info(request, "username already exists")
                return redirect("notes/register.html")
            elif Customer.objects.filter(email=c).exists():
                messages.info(request, "email already exists")
                return redirect("notes/register.html")
            else:
                user = Customer.objects.create(name=a, username=b, email=c, password=d)
                user.save()
                return redirect("http://127.0.0.1:8000/login")
        else:
            messages.info(request, "passwords do not match")
            return render(request, "notes/register.html")
    else:
        return render(request, "notes/register.html")


def login(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        log1 = Customer.objects.filter(username=u, password=p)
        if log1.filter(username=u, password=p).exists():
            for i in log1:
                x = i.username
                y = i.status
                request.session['username'] = u
                request.session['password'] = p
                if y == 'A':
                    return render(request, "notes/admin1.html")
                else:
                    return render(request, "notes/user.html")
        else:
            return render(request, "notes/login.html")
    else:
        return render(request, "notes/login.html")


def logouts(request):
    logout(request)
    return redirect('login')

def editprofile(request):
    # Get the current user object
    username = request.session.get('username')
    user = Customer.objects.get(username=username)

    if request.method == 'POST':
        # Update the user object with new data from the form
        user.name = request.POST.get('name', user.name)
        user.email = request.POST.get('email', user.email)
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            user.password = password
            user.confirmpassword = confirm_password
        else:
            return redirect('profilee')
        user.save()
        return render(request,"notes/user.html")
    else:
        # Render the edit profile form with the current user data
        context = {'user': user}
        return render(request, 'notes/profileedit.html', context)
def profilee(request):
    return render(request,'notes/profileedit.html')

def user(request):
    return render(request,"notes/user.html")

def uploaddash(request):
    c=request.session["username"]
    cus=Customer.objects.get(username=c)
    details = Post.objects.filter(username=cus)
    return render(request,'notes/uploaddash.html', {'details': details})


# crud of file
@login_required
def upload(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            c = request.session["username"]
            cus = Customer.objects.get(username=c)
            post.username = cus
            post.save()
            return redirect("uploaddash")
    else:
        form = PostForm()
    return render(request, 'notes/upload.html', {'form': form})


@login_required
def pdfedit(request, pk):
    c = request.session.get("username")
    cus = get_object_or_404(Customer, username=c)
    pdf = get_object_or_404(Post, pk=pk)
    if cus != pdf.username:  # check if the user owns the document

        return redirect('uploaddash')
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=pdf)
        if form.is_valid():
            form.save()

            return redirect('uploaddash')
    else:
        form = PostForm(instance=pdf)
    return render(request, 'notes/pdfedit.html', {'form': form, 'pdf': pdf})


@login_required
def delete(request, pk):
    c = request.session.get("username")
    cus = get_object_or_404(Customer, username=c)
    pdf = get_object_or_404(Post, pk=pk)
    if cus == pdf.username:  # check if the user owns the document
        pdf.delete()

    return redirect('uploaddash')

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'notes/post_detail.html', {'post': post})
