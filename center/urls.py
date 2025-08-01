from django.urls import path
from .views import *

urlpatterns = [
    path('', ListCreateAPI.as_view(), name='ListCreate'),
    path('detail/<int:pk>/', DetailUpdateDlete.as_view(), name='detail')
]