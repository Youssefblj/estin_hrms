from django.db import models
from employees.models import Fonctionnaire

class Payroll(models.Model):
    fonctionnaire = models.ForeignKey(Fonctionnaire, on_delete=models.CASCADE)
    mois = models.CharField(max_length=20)  # مثل "09/2025"
    salaire_base = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    prime = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Fiche de paie - {self.fonctionnaire.nom} ({self.mois})"
