from django.urls import path
from .import views

urlpatterns = [
    
    path('', views.entry, name='entry'),
    path('ratio', views.ratio, name='ratio'),
    
]
