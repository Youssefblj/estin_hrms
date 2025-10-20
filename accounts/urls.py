from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path("dashboard/admin/", views.admin_dashboard, name="admin_dashboard"),
    path("dashboard/employee/", views.employee_dashboard, name="employee_dashboard"),
    path('edit/', views.edit_account, name='edit_account')

    

]
