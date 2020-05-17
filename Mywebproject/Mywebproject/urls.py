
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from drbotapp import views
from drbotapp import api_view

urlpatterns = [
    url(r'^api/v1/servers/', api_view.rpaserverlist.as_view(),name = "rpaserverlist"),
    url(r'^$', views.index,name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^drbotapp/login/$',views.user_login, name = 'user_login'),
    url(r'^drbotapp/logout/$',views.user_logout, name='logout'),
    url(r'^drbotapp/about/$',views.about, name='about'),
    url(r'^drbotapp/services/$',views.services, name='services'),
    url(r'^drbotapp/contact/$',views.contact, name='contact'),
    url(r'^drbotapp/register/$',views.register, name='register'),
    url(r'^drbotapp/forgot/$',views.forgot, name='forgot'),
    url(r'^drbotapp/manageserver/$',views.manageServer, name='manageServer'),
    url(r'^drbotapp/manageRobot/$', views.manageRobot, name='manageRobot'),
    url(r'^drbotapp/manageMachine/$', views.manageMachine, name='manageMachine'),
    url(r'^drbotapp/manageApp/$', views.manageApp, name='manageApp'),
    url(r'^drbotapp/charts/$', views.charts, name='charts'),
    # url(r'^drbotapp/monitorRobot/$', views.monitorRobot, name='monitorRobot'),
    # url(r'^drbotapp/monitorMachine/$', views.monitorMachine, name='monitorMachine'),
    # url(r'^drbotapp/monitorApp/$', views.monitorApp, name='monitorApp'),
    url(r'^drbotapp/home/$',views.home, name = 'home'),
    url(r'^drbotapp/configdetail/(\d+)/',views.configdetail, name ='configdetail'),
    url(r'^reset/$',   auth_views.PasswordResetView.as_view(
        template_name='password_reset.html',
        email_template_name='password_reset_email.html',
        subject_template_name='password_reset_subject.txt' ),name='password_reset' ),
    url(r'^reset/done/$', auth_views.PasswordResetDoneView.as_view(
            template_name='password_reset_done.html'),  name ='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='password_reset_complete.html'),
        name ='password_reset_complete'),
]