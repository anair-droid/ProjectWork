from django import forms
from django.contrib.auth.models import User
from .models import tblConfig,rpaserverConfig,rparobotconfig, rpabotmachine, rpaappinfo

class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','password')
        # labels = {'username': 'User Name','password': 'Password'}

class UserFormRegister(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')
        # labels = {'username': 'User Name','password': 'Password'}




class tblConfigForm(forms.ModelForm):
    botname =forms.CharField()
    botdescription = forms.CharField()
    application = forms.CharField()

    class Meta():
        model = tblConfig
        fields = ('botname','botdescription','application')


        # class UserForm(forms.Form):
#     username = forms.CharField(label='User Name', max_length=100)
#     password = forms.CharField(label='Password', max_length=32,widget=forms.PasswordInput)

class rpaserverConfigForm(forms.ModelForm):
    applob =forms.CharField()
    appname = forms.CharField()
    appUrl = forms.CharField()
    appAPIkey = forms.CharField()
    param = forms.CharField()

    class Meta():
        model = rpaserverConfig
        fields = ('applob','appname','appUrl','appAPIkey','param')

        # class UserForm(forms.Form):
#     username = forms.CharField(label='User Name', max_length=100)
#     password = forms.CharField(label='Password', max_length=32,widget=forms.PasswordInput)

class rpabotconfigForm(forms.ModelForm):
    botname =forms.CharField()
    botdesc = forms.CharField()
    botServerID = forms.CharField()

    class Meta():
        model = rparobotconfig
        fields = ('botname','botdesc','botServerID')

##Class form for Rpa Machine

class rpabotmachineForm(forms.ModelForm):
    machinename =forms.CharField()
    machineIP = forms.CharField()
    machinedesc = forms.CharField()
    RPAServerID = forms.CharField()
    class Meta():
        model = rpabotmachine
        fields = ('machinename','machineIP','machinedesc','RPAServerID')

##Class form for  Application

class rpaappinfoForm(forms.ModelForm):
    appname =forms.CharField()
    appdesc = forms.CharField()
    applob = forms.CharField()

    class Meta():
        model = rpaappinfo
        fields = ('appname','appdesc','applob')

