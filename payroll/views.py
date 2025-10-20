from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def payroll_view(request):
    if request.user.role != 'accountant' and request.user.role != 'admin':
        return redirect('/accounts/login/')
    return render(request, 'payroll/fiche_paie.html')
