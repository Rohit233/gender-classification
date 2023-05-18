from . import api
from django.urls import path,include
urlpatterns = [
    path('predict-gender',api.predictGender,name='predict-gender')
]