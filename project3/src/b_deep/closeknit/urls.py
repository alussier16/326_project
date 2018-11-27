from django.urls import path
from django.conf.urls import url
from . import views
from django.views.generic import RedirectView


urlpatterns = [
    path('', views.post, name='main'),
]

urlpatterns += [
    path('ties', views.ties, name='ties'),
]

urlpatterns += [
    path('<slug:viewed_account>/account', views.account, name='account'),
]

urlpatterns += [
    path('sign-up', views.signup, name='signup'),
]

urlpatterns += [
    path('account-created', views.accountcreated, name='accountcreated'),
]

urlpatterns += [
    path('settings', views.settings, name='settings'),
]

urlpatterns += [
    path('addfriend', views.addfriend, name='addfriend'),
]

urlpatterns += [
    path('login', views.log_in, name='login'),
]

urlpatterns += [
    path('logout', views.log_out, name='log_out'),
]

urlpatterns += [
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment, name='add-comment'),
]

urlpatterns += [
    path('add-post', views.add_post, name='add-post'),
]

urlpatterns += [
    path('', RedirectView.as_view(url='registration/login')),
]

