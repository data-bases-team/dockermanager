from django.urls import path, include
from . import views
from users.views import dashboard

urlpatterns = [
    path('accounts/', include("django.contrib.auth.urls")),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('register/', views.register, name="register"),
    path('run_script/', views.run_script, name='run_script'),
]