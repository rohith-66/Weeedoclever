from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

from django.conf import settings
from django.core import mail
from django.core.mail.message import EmailMessage





def index(request):

    return render(request,'index.html')

def handleSignup(request):
    if request.method == 'POST':

        # TAKE THE PARAMETERS FROM THE POP UP FORM
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        if len(fname)<2 or len(email)<3 or len(username)<10:
            messages.error(request,"  please fill the valid details") 


        if len(username)>15:
            messages.error(request,"username should be less than 15 characters")
            return redirect('/')

        

        if User.objects.filter(username=username).exists():
            messages.error(request,"USN already taken,Please try to Login...")
            return redirect('/')


            

        if not username.isalnum():
            messages.error(request,"username should contain only letters and there should be no space")
            return redirect('/')

        if pass1 != pass2:
            messages.error(request,"invali passoword")
            return redirect('/')


           
            
        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,"Successfully Signed  In")
        return redirect('/')





def handleLogin(request):

    if request.method == "POST":

        # GET PARAMETERS
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']
        user=authenticate(username=loginusername,password=loginpassword)
        if user is not None:

            login(request,user)
            messages.success(request,"Successfully Logged In")
            return redirect('/')
        else:
            messages.error(request,"Invalid Credentials")
           
            return redirect('/')


def handleLogout(request):
    logout(request)
    messages.success(request,"Successfully Logged Out")
    return redirect('/')



def notes(request):
        if not request.user.is_authenticated:
             messages.error(request,"Please login")
             return render(request,'index.html') 

        else:

            return render(request,'notes.html')

def assignments(request):
        if not request.user.is_authenticated:
             messages.error(request,"Please login")
             return render(request,'index.html') 

        else:

            return render(request,'assignments.html')

def questions(request):
        if not request.user.is_authenticated:
             messages.error(request,"Please login")
             return render(request,'index.html') 

        else:

            return render(request,'questions.html')

def about(request):
            return render(request,'about.html')

