from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponse
from django.http import Http404
from .forms import UserForm, UserFormRegister
from .models import Contact,tblConfig,rparobotconfig,rpaserverConfig,rpabotmachine,rpaappinfo
from datetime import datetime
from django.contrib import messages


# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth

from .models import tblConfig
from .process_check import get_size,get_processes_info,construct_dataframe
# Create your views here.

def index(request):
    return render(request,'drbotapp/index.html')

@login_required
def special(request):
    # Remember to also set login url in settings.py!
    # LOGIN_URL = '/basic_app/user_login/'
    return HttpResponse("You are logged in. Nice!")

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))

def services(request):
    return render(request, 'drbotapp/services.html')
    #return HttpResponse("this is services")

def about(request):
    return render(request, 'drbotapp/about.html')
   # return HttpResponse("this is about")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact= Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'drbotapp/contact.html')



def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            # Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request, user)
                # Send the user back to some page.
                # In this case their homepage.
                # tblConfs = tblConfig.objects.all()
                # return render(request, 'drbotapp/home.html', {'drbotdetail': tblConfs})
                return HttpResponseRedirect(reverse('index'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print(authenticate(username=username, password=password))
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    else:
        # Nothing has been provided for username or password.
        loginpg = UserForm()
        return render(request,'drbotapp/Login.html',{'drbotlogin': loginpg})


@login_required
def home(request):
    return render(request, 'drbotapp/home.html')


# def configuration(request):
#     user_frmvalues = UserFormRegister()
#     user_profile = UserProfileForm()
#     return render(request,'drbotapp/configure.html' ,{'user_config': user_frmvalues,'profil_Config': user_profile })

@login_required
def configdetail(request,id):

    try:
        tblConf = tblConfig.objects.get(id=id)
    except tblConfig.DoesNotExist:
        raise Http404('Config not found')
    return render(request,'drbotapp/configdetail.html', {'tblConf':tblConf} )


@login_required
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'usernameTaken')
                print('username taken')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email-Id Is Already Exits')
                print('email exits')
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, password=password1, first_name=first_name,
                                                last_name=last_name, email=email)
                user.save()
                print('user created')
                return redirect("/")


        else:
            print('password not matched')
            return redirect('register')
            # return redirect("/")
    else:
        return render(request, 'drbotapp/register.html')


@login_required
def manageRobot(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            botname = request.POST.get('botname')
            botdesc = request.POST.get('botdesc')
            botServerID = request.POST.get('botServerID')
            botinfo = rparobotconfig(botname=botname, botdesc=botdesc, botServerID=botServerID)
            botinfo.save()
            messages.success(request, 'Data Saved!')
        rpadata = rparobotconfig.objects.all()
        return render(request, 'drbotapp/monitorRobot.html', {'monitorBot': rpadata})
    else:
        # Nothing has been provided for username or password.
        # loginpg = UserForm()
        # return render(request, 'drbotapp/Login.html', {'drbotlogin': loginpg})
        return HttpResponseRedirect(reverse('index'))

# def monitorRobot(request):
#     if request.user.is_authenticated:
#         rpadata = rparobotconfig.objects.all()
#         return render(request, 'drbotapp/monitorRobot.html', {'monitorBot': rpadata})
#         # return HttpResponseRedirect(reverse('index'))
#     else:
#         # Nothing has been provided for username or password.
#         # loginpg = UserForm()
#         # return render(request, 'drbotapp/Login.html', {'drbotlogin': loginpg})
#         return HttpResponseRedirect(reverse('index'))
@login_required
def manageServer(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            applob = request.POST.get('applob')
            appname = request.POST.get('appname')
            appUrl = request.POST.get('appUrl')
            appAPIkey = request.POST.get('appAPIkey')
            param = request.POST.get('param')
            serverinfo = rpaserverConfig(applob=applob, appname=appname, appUrl=appUrl,appAPIkey = appAPIkey,param=param)
            serverinfo.save()
            messages.success(request, 'Data Saved!')
        rpasvrr = rpaserverConfig.objects.all()
        return render(request, 'drbotapp/monitorServer.html', {'monitorSvr': rpasvrr})
    else:
        # Nothing has been provided for username or password.
        # loginpg = UserForm()
        # return render(request, 'drbotapp/Login.html', {'drbotlogin': loginpg})
        return HttpResponseRedirect(reverse('index'))

# def monitorServer(request):
#     if request.user.is_authenticated:
#         rpasvrr = rpaserverConfig.objects.all()
#         return render(request, 'drbotapp/monitorServer.html', {'monitorSvr': rpasvrr})
#         # return HttpResponseRedirect(reverse('index'))
#     else:
#         # Nothing has been provided for username or password.
#         # loginpg = UserForm()
#         # return render(request, 'drbotapp/Login.html', {'drbotlogin': loginpg})
#         return HttpResponseRedirect(reverse('index'))
@login_required
def manageMachine(request):
    if request.user.is_authenticated:
            if request.method == "POST":
                machinename = request.POST.get('machinename')
                machineIP = request.POST.get('machineIP')
                machinedesc = request.POST.get('machinedesc')
                RPAServerID = request.POST.get('RPAServerID')
                tbleinfo = rpabotmachine(machinename=machinename, machineIP=machineIP, machinedesc=machinedesc,RPAServerID = RPAServerID)
                tbleinfo.save()
                messages.success(request, 'Data Saved!')
                # return render(request, 'drbotapp/monitorMachine.html')
            rpadata = rpabotmachine.objects.all()
            # rpadata = construct_dataframe(get_processes_info())
            # Htm = rpadata.to_html()
            return render(request, 'drbotapp/monitorMachine.html', {'monitorMachine': rpadata})
            # return HttpResponseRedirect(reverse('index'))
    else:
        # Nothing has been provided for username or password.
        # loginpg = UserForm()
        # return render(request, 'drbotapp/Login.html', {'drbotlogin': loginpg})
        return HttpResponseRedirect(reverse('index'))

# def monitorMachine(request):
#     if request.user.is_authenticated:
#         rpadata = rpabotmachine.objects.all()
#         # rpadata = construct_dataframe(get_processes_info())
#         # Htm = rpadata.to_html()
#         return render(request, 'drbotapp/monitorMachine.html', {'monitorMachine': rpadata})
#         # return HttpResponseRedirect(reverse('index'))
#     else:
#         # Nothing has been provided for username or password.
#         # loginpg = UserForm()
#         # return render(request, 'drbotapp/Login.html', {'drbotlogin': loginpg})
#         return HttpResponseRedirect(reverse('index'))
@login_required
def manageApp(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            appname = request.POST.get('machinename')
            appdesc = request.POST.get('machineIP')
            applob = request.POST.get('machinedesc')
            tbleinfo = rpaappinfo(appname=appname, appdesc=appdesc, applob=applob)
            tbleinfo.save()
            messages.success(request, 'Data Saved!')
        rpadata = rpaappinfo.objects.all()
        return render(request, 'drbotapp/monitorApp.html', {'monitorApp': rpadata})
    else:
        # Nothing has been provided for username or password.
        # loginpg = UserForm()
        # return render(request, 'drbotapp/Login.html', {'drbotlogin': loginpg})
        return HttpResponseRedirect(reverse('index'))

# def monitorApp(request):
#     if request.user.is_authenticated:
#         rpadata = rpaappinfo.objects.all()
#         return render(request, 'drbotapp/monitorApp.html', {'monitorApp': rpadata})
#         # return HttpResponseRedirect(reverse('index'))
#     else:
#         # Nothing has been provided for username or password.
#         # loginpg = UserForm()
#         # return render(request, 'drbotapp/Login.html', {'drbotlogin': loginpg})
#         return HttpResponseRedirect(reverse('index'))



def forgot(request):
    auth.logout(request)
    return redirect("password_reset")

@login_required
def charts(request):
    rpadata = rpabotmachine.objects.all()
    return render(request, 'drbotapp/Chartpage.html',{'chartMachData': rpadata})

