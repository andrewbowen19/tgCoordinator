from django.urls import path, include

from . import views
from django.contrib.auth import authenticate, login
from django.conf.urls import url

from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    # index should be main user page - where guides can access their results
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/plot/', views.plot, name='plot'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='templates/registration/login.html')),

]








