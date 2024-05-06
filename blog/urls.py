from django.urls import path
from blog.views import indexes
from django.urls import path,include

urlpatterns = [
    path('',indexes),
]