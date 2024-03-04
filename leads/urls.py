from django.urls import path

from . import views

urlpatterns = [
    path('', views.LandingPageView.as_view(), name='home'),
    path('lead_list/', views.LeadListView.as_view(), name='lead_list'),
    path('<int:pk>', views.LeadDetailView.as_view(), name='lead_detail'),
    path('<int:pk>/lead_update', views.LeadUpdateView.as_view(), name='lead_update'),
    path('<int:pk>/lead_delete', views.LeadDeleteView.as_view(), name='lead_delete'),
    path('<int:pk>/assign_agent', views.AssignAgentView.as_view(), name='assign_agent'),
    path('lead_create', views.LeadCreateView.as_view(), name='lead_create'),
    path('categories', views.CategoryListView.as_view(), name='category_list'),


]