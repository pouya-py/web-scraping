from django.urls import path
from django.urls.resolvers import URLPattern
from . import views


app_name = 'ml'
urlpatterns = [
    path('', views.predict_price, name='prediction')
]