from django.contrib import admin
from django.urls import path
from employees import views as emp_views  # import employee views
from accounts import views as acc_views  # import accounts views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', acc_views.login_view, name='login'),  # default route
    path('register/', acc_views.register_view, name='register'),
    path('employee/dashboard/', emp_views.employee_dashboard, name='employee_dashboard'),
    path('ats/list/', emp_views.ats_list, name='ats_list'),
    path('fonctionnaires/', emp_views.fonctionnaires_list, name='fonctionnaires_list'),
    path('logout/', acc_views.logout_view, name='logout'),
]
