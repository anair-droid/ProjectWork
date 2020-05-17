from django.contrib import admin
from .models import tblConfig
from .models import Contact,rpaappinfo,rpabotmachine,rparobotconfig,rpaserverConfig

# Register your models here.


@admin.register(tblConfig,Contact,rpaappinfo,rpabotmachine,rparobotconfig,rpaserverConfig)
class tblconfigAdmin(admin.ModelAdmin):
    pass