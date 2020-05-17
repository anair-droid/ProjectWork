from django.db import models



class tblConfig(models.Model):
    botname = models.CharField(max_length=100)
    botdescription = models.CharField(max_length=100)
    application = models.CharField(max_length=40)


class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=40)
    desc=models.TextField()
    date=models.DateField()

class rpaserverConfig(models.Model):
    applob = models.CharField(max_length=100)
    appname = models.CharField(max_length=100)
    appUrl = models.URLField(blank=True)
    appAPIkey = models.CharField(max_length=100)
    param = models.CharField(max_length=100)

class rparobotconfig(models.Model):
    botname = models.CharField(max_length=100)
    botdesc = models.CharField(max_length=100)
    botServerID = models.CharField(max_length=100)


class rpabotmachine(models.Model):
    machinename = models.CharField(max_length=100)
    machineIP = models.CharField(max_length=100)
    machinedesc = models.CharField(max_length=100)
    RPAServerID = models.CharField(max_length=100)
    NumberofBots = models.IntegerField()

class rpaappinfo(models.Model):
    appname = models.CharField(max_length=100)
    appdesc = models.CharField(max_length=100)
    applob = models.CharField(max_length=100)