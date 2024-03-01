from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lead_list/', views.lead_list, name='lead_list'),
    path('<int:pk>', views.lead_detail, name='lead_detail'),
    path('<int:pk>/lead_update', views.lead_update, name='lead_update'),
    path('<int:pk>/lead_delete', views.lead_delete, name='lead_delete'),
    path('lead_create', views.lead_create, name='lead_create'),

]