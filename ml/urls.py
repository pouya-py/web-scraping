from django.urls import path,include
from django.urls.resolvers import URLPattern
from . import views
from .machine_learning import _


app_name = 'ml'
urlpatterns = [
    path('predict/', views.predict_price(), name='prediction')
]