from django.shortcuts import render,HttpResponseRedirect,reverse
from .models import *
from random import *
from .utils import *
# Create your views here.


def IndexPage(request):
    return render(request,"app/index2.html")

def JSPage(request):
    return render(request,"app/JsForm.html")

def LoginPage(request):
    return render(request,"app/login.html")

def WelcomePage(request):
    return render(request,"app/welcome.html")

def RegisterUser(request):
    if request.POST['role']=="employee":
        role = request.POST['role']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        gender = request.POST['gender']
        # pic = request.FILES['image/tt']

        user = User.objects.filter(Email=email)
        if user:
            message = "User already Exist"
            return render(request,"app/index2.html",{'msg':message})
        else:
            if password==cpassword:
                otp = randint(100000,999999)
                newuser = User.objects.create(role=role,Email=email,Password=password,otp=otp)
                newemp = Employee.objects.create(user_id=newuser,Firstname=fname,Lastname=lname,
                gender=gender)
                email_Subject = "Employee Verification Mail"
                sendmail(email_Subject,'mail_template',email,{'name':fname,'otp':otp})
                return render(request,"app/welcome.html")
            else:
                message = "Password Doesnot match"
                return render(request,"app/index2.html",{'msg':message})
    else:
        print("Hirer Coming Soon")




def LoginEvaluation(request):
    if request.POST['role']=="employee":
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.get(Email=email)
        if user:
            if user.Password == password and user.role=="employee":
                newemp = Employee.objects.get(user_id=user)
                request.session['email'] = user.Email
                request.session['Firstname'] = newemp.Firstname
                request.session['id'] = user.id
                request.session['role'] = user.role

                return HttpResponseRedirect(reverse('homepage'))
            else:
                message = "Password Doesnot Match"
                return render(request,"app/login.html",{'msg':message})
        else:
            message = "User doesnot Exist"
            return render(request,"app/login.html",{'msg':message})
    else:
        print("Hirer Coming Soon")


def Hompage(request):
    if 'email' in request.session and 'role' in request.session:
        if request.session['role'] == "employee":
            all_emp = Employee.objects.all()
            all_user = User.objects.all()
            return render(request,"app/home.html",{'hp_key':all_emp,'user_key':all_user})
        else:
            print("Hirer in session coming soon")
    else:
        msg = "Unauthorized Person"
        return render(request,"app/login.html",{'msg':msg})


def Logout(request):
    del request.session['email']
    del request.session['Firstname']
    return HttpResponseRedirect(reverse('login'))