from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_planworkouts, name='planworkouts'),
    path('<int:Planworkout_id>/', views.planworkout_detail, name='planworkout_detail')
]