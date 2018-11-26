from django.urls import path
from . import views

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