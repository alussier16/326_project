from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
]

urlpatterns += [
    path('ties', views.ties, name='ties'),
]

urlpatterns += [
    path('account', views.account, name='account'),
]

urlpatterns += [
    path('sign-up', views.signup, name='signup'),
]

urlpatterns += [
    path('login', views.login, name='login'),
]

urlpatterns += [
    path('account-created', views.accountcreated, name='accountcreated'),
]
