from django.urls import path
from .import views
urlpatterns=[
    path('new',views.loginpage,name="first"),
    path('start' ,views.newpage,name="second"),
    path('next',views.masterpage,name="third")
]
