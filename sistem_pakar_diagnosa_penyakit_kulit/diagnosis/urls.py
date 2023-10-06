from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="diagnosa" ),
    path('form/', views.form, name="diagnosa-form" ),
    path('hasil/', views.hasil, name="diagnosa-hasil" ),
]