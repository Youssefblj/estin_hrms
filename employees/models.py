from django.db import models
from datetime import date
from django.db import models
from django.conf import settings
from datetime import date



class Fonctionnaire(models.Model):
    ss = models.CharField(max_length=20, unique=True, verbose_name="S-S")
    nom = models.CharField(max_length=50, verbose_name="Nom")
    prenom = models.CharField(max_length=50, verbose_name="Prénom")
    grade = models.CharField(max_length=50, verbose_name="Grade")
    date_rec = models.DateField(verbose_name="Date de recrutement")
    statut = models.CharField(max_length=20, default='Actif')
    telephone = models.CharField(max_length=20, verbose_name="Numéro", null=True, blank=True)


    def __str__(self):
        return f"{self.nom} {self.prenom}"

class Employee(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    base_salary = models.DecimalField(max_digits=10, decimal_places=2)
    bonus = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date_rec = models.DateField(default=date.today, verbose_name="Date de recrutement")

    def total_salary(self):
        return self.base_salary + self.bonus - self.deductions

    def __str__(self):
        return self.user.username
    

class LeaveRequest(models.Model):
    LEAVE_TYPES = [
        ('ANNUAL', 'Annual Leave'),
        ('SICK', 'Sick Leave'),
        ('UNPAID', 'Unpaid Leave'),
        ('OTHER', 'Other'),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)  # ✅ تغيير هنا
    leave_type = models.CharField(max_length=20, choices=LEAVE_TYPES, default='ANNUAL')
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=20, default='Pending')
    date_submitted = models.DateField(default=date.today)

    def __str__(self):
        return f"{self.employee.user.username} - {self.leave_type} ({self.status})"
    
class CareerHistory(models.Model):      
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    position_title = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.employee.user.username} - {self.position_title}"
    
    
class Paie(models.Model):
    fonctionnaire = models.ForeignKey(Fonctionnaire, on_delete=models.CASCADE)
    mois = models.CharField(max_length=20)
    annee = models.IntegerField()
    salaire_base = models.DecimalField(max_digits=10, decimal_places=2)
    indemnites = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    retenues = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    net_a_payer = models.DecimalField(max_digits=10, decimal_places=2)
    date_ajout = models.DateTimeField(auto_now_add=True)


class Prime(models.Model):
    fonctionnaire = models.ForeignKey(Fonctionnaire, on_delete=models.CASCADE)
    type_prime = models.CharField(max_length=100)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_prime = models.DateField()


class Conge(models.Model):
    fonctionnaire = models.ForeignKey(Fonctionnaire, on_delete=models.CASCADE)
    type_conge = models.CharField(max_length=100)
    date_debut = models.DateField()
    date_fin = models.DateField()
    motif = models.TextField()
    def __str__(self):
        return f"{self.type_conge} ({self.fonctionnaire})"

class Promotion(models.Model):
    fonctionnaire = models.ForeignKey(Fonctionnaire, on_delete=models.CASCADE)
    date_promotion = models.DateField(null=True, blank=True)

    nouveau_grade = models.CharField(max_length=100)
    observation = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Promotion - {self.fonctionnaire.nom} {self.fonctionnaire.prenom}"


class Echelon(models.Model):
    fonctionnaire = models.ForeignKey(Fonctionnaire, on_delete=models.CASCADE)
    date_echelon = models.DateField(null=True, blank=True)

    
    nouvel_echelon = models.IntegerField(null=True, blank=True)

    observation = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Echelon - {self.fonctionnaire.nom} {self.fonctionnaire.prenom}"


class Historique(models.Model):
    fonctionnaire = models.ForeignKey(Fonctionnaire, on_delete=models.CASCADE)
    date_action = models.DateField(auto_now_add=True)
    type_action = models.CharField(max_length=100)
    details = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Historique - {self.fonctionnaire.nom} {self.fonctionnaire.prenom}"


