"""testproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import TeleGuestApp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TeleGuestApp.views.index,name="index"),
    path('create/',TeleGuestApp.views.create,name="create"),
    path('detail/<int:pk>',TeleGuestApp.views.detail,name="detail"),
    path('update/<int:pk>',TeleGuestApp.views.update,name="update"),
    path('delete/<int:pk>',TeleGuestApp.views.delete,name="delete"),
    path('participate/<int:pk>',TeleGuestApp.views.participate, name="participate"),
    path('unparticipate/<int:pk>',TeleGuestApp.views.unparticipate,name="unparticipate"),
    path('reserve',TeleGuestApp.views.reserve,name="reserve"),
    path('reserve_house',TeleGuestApp.views.reserve_house,name="reserve_house"),
    path('reserve_finish',TeleGuestApp.views.reserve_finish,name="reserve_finish"),
]
