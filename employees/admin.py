from django.contrib import admin
from .models import Fonctionnaire
from .models import CareerHistory
from .models import Employee
from .models import Paie,Prime,Conge,Promotion,Echelon,Historique,LeaveRequest

@admin.register(Fonctionnaire)
class FonctionnaireAdmin(admin.ModelAdmin):
    list_display = ('ss', 'nom', 'prenom', 'grade', 'date_rec', 'statut','telephone')
    search_fields = ('nom', 'prenom', 'ss')




@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'position', 'base_salary', 'bonus', 'deductions', 'total_salary_display')
    search_fields = ('user__username', 'position')
    list_filter = ('position',)

    def total_salary_display(self, obj):
        return obj.total_salary()
    total_salary_display.short_description = 'Total Salary'
    
    
    admin.site.register(CareerHistory)
    admin.site.register(Paie)
    admin.site.register(Prime)
    admin.site.register(Conge)
    admin.site.register(Promotion)
    admin.site.register(Echelon)
    admin.site.register(Historique)
    admin.site.register(LeaveRequest)
    
    