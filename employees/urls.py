from django.urls import path
from . import views

urlpatterns = [
    path('', views.fonctionnaires_list, name='fonctionnaires_list'),
    path('dashboard/', views.employee_dashboard, name='employee_dashboard'),
    path('list_ats/', views.list_ats, name='list_ats'),
    path('delete_ats/<int:pk>/', views.delete_ats, name='delete_ats'),
    path('fonctionnaires/', views.fonctionnaires_list, name='fonctionnaires_list'),
    path('user-space/', views.user_space, name='user_space'),
    path('ats-space/', views.ats_space, name='ats_space'),

    path('fonctionnaires/add/', views.add_fonctionnaire, name='add_fonctionnaire'),
    path('fonctionnaires/edit/<int:pk>/', views.edit_fonctionnaire, name='edit_fonctionnaire'),
    path('fonctionnaires/delete/<int:pk>/', views.delete_fonctionnaire, name='delete_fonctionnaire'),
    path('fonctionnaires/<int:pk>/', views.fonctionnaire_detail, name='fonctionnaire_detail'),

    
   
    
    path('salary-slip/', views.salary_slip, name='salary_slip'),
    path('work-certificate/', views.work_certificate, name='work_certificate'),
    path('leave-request/', views.leave_request, name='leave_request'),
    path('career-history/', views.career_history, name='career_history'),
    
    
    path('work-certificate/download/', views.download_certificate, name='download_certificate'),
    
     # --- Mise à jour ---
    path('<int:pk>/paie/', views.update_paie, name='update_paie'),
    path('<int:pk>/promotion/', views.update_promotion, name='update_promotion'),
    path('<int:pk>/echelon/', views.update_echelon, name='update_echelon'),
    path('<int:pk>/prime/', views.update_prime, name='update_prime'),
    path('<int:pk>/conge/', views.update_conge, name='update_conge'),
    path('<int:pk>/historique/', views.view_historique, name='view_historique'),

    # --- Imprimer ---
    path('<int:pk>/fiche_paie/', views.print_fiche_paie, name='print_fiche_paie'),
    path('<int:pk>/attestation_travail/', views.print_attestation_travail, name='print_attestation_travail'),
    path('<int:pk>/titre_conge/', views.print_titre_conge, name='print_titre_conge')
]
