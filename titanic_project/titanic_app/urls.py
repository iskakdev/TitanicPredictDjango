from django.urls import path
from .views import TitanicPredict

urlpatterns = [
    path('predict/', TitanicPredict.as_view(), name='titanic_predict')
]