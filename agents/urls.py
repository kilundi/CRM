from django.urls import path

from. import views

app_name = 'agents'

urlpatterns = [
    path('agents_list/', views.AgentListView.as_view(), name='agents_list'),
    path('create_agent/', views.AgentCreateView.as_view(), name='create_agent'),
    path('<int:pk>/', views.AgentDetailView.as_view(), name='agent_details'),
    path('<int:pk>/agent_update', views.AgentUpdateView.as_view(), name='agent_update'),
     path('<int:pk>/agent_delete', views.AgentDeleteView.as_view(), name='agent_delete'),

]