from django.urls import path, include
from . import views
from users.views import dashboard

urlpatterns = [
    path('accounts/', include("django.contrib.auth.urls")),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('', views.dashboard, name="dashboard"),
    path('register/', views.register, name="register"),
    path('run_script_start/', views.run_script_start, name='run_script_start'),
    path('run_script_end/', views.run_script_end, name='run_script_end'),
    path('run_script_prolong/', views.run_script_prolong, name='run_script_prolong'),
    path('run_script_new/', views.run_script_new, name='run_script_new'),
    path('run_script_delete/', views.run_script_delete, name='run_script_delete'),
    path('add/',views.add_container, name='add_container',),
    path('delete/<str:container_name>',views.delete_container, name='delete_container',),
    path('restatus/<str:container_name>',views.restatus_container, name='restatus_container',),
    path('prolong/<str:container_name>',views.prolong_container, name='prolong_container',),
    
]