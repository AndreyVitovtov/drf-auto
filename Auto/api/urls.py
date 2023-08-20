from django.urls import path

from . import views

urlpatterns = [
    path('autos/', views.auto),
    path('auto/<int:id>', views.auto),
    path('owners', views.owner),
    path('owner/<int:id>', views.owner),
    path('passport', views.autos_passport),
    path('passport/<int:id>', views.autos_passport),
]
