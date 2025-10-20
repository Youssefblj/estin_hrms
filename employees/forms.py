from django import forms
from .models import Fonctionnaire
from django.db import models
from django.conf import settings
from datetime import date
from .models import LeaveRequest
from django import forms
from .models import Paie, Prime, Conge,Historique,Promotion,Echelon


class FonctionnaireForm(forms.ModelForm):
    class Meta:
        model = Fonctionnaire
        fields = ['ss', 'nom', 'prenom', 'grade', 'date_rec','statut','telephone']
        widgets = {
            'date_rec': forms.DateInput(attrs={'type': 'date'}),
        }
        

        
class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        fields = ['leave_type', 'start_date', 'end_date', 'reason']
        widgets = {
            'leave_type': forms.Select(attrs={'class': 'form-select'}),
            'start_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'end_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'reason': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Explain your reason...',
                'class': 'form-control'
            }),
        }
        
  # تأكد أن هذه النماذج موجودة عندك في models.py

class PaieForm(forms.ModelForm):
    class Meta:
        model = Paie
        fields = ['mois', 'annee', 'salaire_base', 'indemnites', 'retenues', 'net_a_payer']
        widgets = {
            'mois': forms.TextInput(attrs={'class': 'form-control'}),
            'annee': forms.NumberInput(attrs={'class': 'form-control'}),
            'salaire_base': forms.NumberInput(attrs={'class': 'form-control'}),
            'indemnites': forms.NumberInput(attrs={'class': 'form-control'}),
            'retenues': forms.NumberInput(attrs={'class': 'form-control'}),
            'net_a_payer': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class PrimeForm(forms.ModelForm):
    class Meta:
        model = Prime
        fields = ['type_prime', 'montant', 'date_prime']
        widgets = {
            'type_prime': forms.TextInput(attrs={'class': 'form-control'}),
            'montant': forms.NumberInput(attrs={'class': 'form-control'}),
            'date_prime': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class CongeForm(forms.ModelForm):
    class Meta:
        model = Conge
        fields = ['type_conge', 'date_debut', 'date_fin', 'motif']
        widgets = {
            'type_conge': forms.TextInput(attrs={'class': 'form-control'}),
            'date_debut': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'date_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'motif': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class PromotionForm(forms.ModelForm):
    class Meta:
        model = Promotion
        fields = ['date_promotion', 'nouveau_grade', 'observation']
        widgets = {
            'date_promotion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'nouveau_grade': forms.TextInput(attrs={'class': 'form-control'}),
            'observation': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class EchelonForm(forms.ModelForm):
    class Meta:
        model = Echelon
        fields = ['date_echelon', 'nouvel_echelon', 'observation']
        widgets = {
            'date_echelon': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'nouvel_echelon': forms.NumberInput(attrs={'class': 'form-control'}),
            'observation': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class HistoriqueForm(forms.ModelForm):
    class Meta:
        model = Historique
        fields = ['type_action', 'details']
        widgets = {
            'type_action': forms.TextInput(attrs={'class': 'form-control'}),
            'details': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
