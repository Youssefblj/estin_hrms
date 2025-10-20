from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .forms import FonctionnaireForm
from .models import Employee
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from datetime import date
from reportlab.lib import colors
from django.contrib import messages
from .forms import LeaveRequestForm
from .models import LeaveRequest, Employee,CareerHistory
from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee
from .forms import PaieForm, PrimeForm, CongeForm
from .models import Fonctionnaire, Promotion, Echelon, Historique,Paie,Conge
from .forms import PromotionForm, EchelonForm, HistoriqueForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import Employee

# قائمة الموظفين (Fonctionnaires)
@login_required
def fonctionnaires_list(request):
    query = request.GET.get('q')
    fonctionnaires = Fonctionnaire.objects.all()

    if query:
        fonctionnaires = fonctionnaires.filter(nom__icontains=query)

    paginator = Paginator(fonctionnaires, 5)
    page = request.GET.get('page')
    fonctionnaires = paginator.get_page(page)

    return render(request, 'employees/fonctionnaires_list.html', {
        'fonctionnaires': fonctionnaires,
        'show_footer': True  # ✅ هذا السطر يجعل الفوتر يظهر فقط في هذه الصفحة
    })



# إضافة موظف جديد
@login_required
def add_fonctionnaire(request):
    if request.method == 'POST':
        form = FonctionnaireForm(request.POST)
        if form.is_valid():
            form.save()

            # detect from where the request came (User Space or Fonctionnaires List)
            next_url = request.POST.get('next', 'fonctionnaires_list')
            return redirect(next_url)
    else:
        form = FonctionnaireForm()

    return render(request, 'employees/fonctionnaire_form.html', {'form': form, 'title': 'Ajouter Fonctionnaire'})


@login_required
def edit_fonctionnaire(request, pk):
    fonctionnaire = get_object_or_404(Fonctionnaire, pk=pk)
    if request.method == 'POST':
        form = FonctionnaireForm(request.POST, instance=fonctionnaire)
        if form.is_valid():
            form.save()

            # Redirect dynamically depending on source
            next_url = request.POST.get('next', 'fonctionnaires_list')
            return redirect(next_url)
    else:
        form = FonctionnaireForm(instance=fonctionnaire)

    return render(request, 'employees/fonctionnaire_form.html', {'form': form, 'title': 'Modifier Fonctionnaire'})


@login_required
def delete_fonctionnaire(request, pk):
    fonctionnaire = get_object_or_404(Fonctionnaire, pk=pk)
    fonctionnaire.delete()

    # dynamic redirect too
    next_page = request.GET.get('next', 'fonctionnaires_list')
    return redirect(next_page)


# باقي الصفحات
@login_required
def employee_dashboard(request):
    return render(request, 'accounts/employee_dashboard.html')

@login_required
def ats_list(request):
    return render(request, 'employees/ats_list.html')
    

@login_required
def user_space(request):
    query = request.GET.get('q')
    fonctionnaires = Fonctionnaire.objects.all().order_by('-date_rec')

    if query:
        fonctionnaires = fonctionnaires.filter(nom__icontains=query)

    context = {
        'users': fonctionnaires,  # ‘users’ is what the template expects
        'query': query,
        
    }
    return render(request, 'employees/user_space.html', context)

@login_required
def ats_space(request):
    return render(request, 'employees/ats_space.html')




def salary_slip(request):
    employee = Employee.objects.get(user=request.user)
    return render(request, 'employees/atsspace/salary_slip.html', {'employee': employee})


@login_required
def work_certificate(request):
    employee = get_object_or_404(Employee, user=request.user)
    
    context = {
        'employee': employee,
        'today': date.today(),
    }
    return render(request, 'employees/atsspace/work_certificate.html', context)



@login_required
def download_certificate(request):
    # Get logged-in employee
    employee = get_object_or_404(Employee, user=request.user)

    # Prepare PDF response
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="work_certificate_{employee.user.username}.pdf"'

    # Initialize PDF
    p = canvas.Canvas(response, pagesize=A4)
    width, height = A4

    # === HEADER ===
    p.setFont("Helvetica-Bold", 24)
    p.setFillColor(colors.HexColor("#1F4E79"))
    p.drawCentredString(width / 2, height - 80, "ESTIN HRMS")
    
    p.setStrokeColor(colors.black)
    p.setLineWidth(1)
    p.line(80, height - 90, width - 80, height - 90)

    # === TITLE ===
    p.setFont("Helvetica-Bold", 20)
    p.setFillColor(colors.black)
    p.drawCentredString(width / 2, height - 150, "Certificate of Employment")

    # === BODY TEXT ===
    p.setFont("Helvetica", 12)
    p.setFillColor(colors.black)

    full_name = employee.user.get_full_name() or employee.user.username.capitalize()

    text = f"""
This is to certify that {full_name} has been employed as a {employee.position} at ESTIN.

The employee has been serving since {employee.date_rec.strftime('%B %d, %Y')} and has continuously 
demonstrated dedication, professionalism, and commitment to excellence.

This certificate is issued upon request of the employee for any official purpose.

Issued on {date.today().strftime('%B %d, %Y')}.
    """

    text_object = p.beginText(80, height - 220)
    text_object.setLeading(18)
    text_object.textLines(text)
    p.drawText(text_object)

    # === SIGNATURE SECTION ===
    p.setFont("Helvetica-Bold", 12)
    p.drawString(80, 150, "_________________________")
    p.drawString(80, 135, "HR Department")
    p.drawString(80, 120, "ESTIN HRMS")

    # === FOOTER ===
    p.setFont("Helvetica-Oblique", 10)
    p.setFillColor(colors.grey)
    p.drawCentredString(width / 2, 60, "This document was generated electronically by ESTIN HRMS.")

    # Save the PDF
    p.showPage()
    p.save()

    return response



@login_required
def leave_request(request):
    # نحصل على الموظف المرتبط بالمستخدم الحالي
    employee = get_object_or_404(Employee, user=request.user)

    if request.method == 'POST':
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            leave_request = form.save(commit=False)
            leave_request.employee = employee  # ✅ هنا نربط الكائن الصحيح
            leave_request.save()
            messages.success(request, " ✅ Your leave request has been submitted successfully.")
            return redirect('leave_request')
        else:
            messages.error(request, "❌ Please check the form fields and try again.")
    else:
        form = LeaveRequestForm()
        


    # ✅ هنا نعرض الطلبات الخاصة بهذا الموظف فقط
    user_requests = LeaveRequest.objects.filter(employee=employee).order_by('-date_submitted')

    return render(request, 'employees/atsspace/leave_request.html', {
        'form': form,
        'user_requests': user_requests,
    })





@login_required
def career_history(request):
    employee = get_object_or_404(Employee, user=request.user)
    history = CareerHistory.objects.filter(employee=employee).order_by('-start_date')

    return render(request, 'employees/atsspace/career_history.html', {
        'employee': employee,
        'history': history,
    })




@login_required
def list_ats(request):
    # البحث عن موظف بواسطة الاسم أو المنصب
    query = request.GET.get('q')
    if query:
        employees = Employee.objects.filter(user__username__icontains=query)
    else:
        employees = Employee.objects.all().order_by('-date_rec')

    context = {
        'employees': employees,
        'query': query,
        'show_footer': True,  # ✅ هذا السطر يجعل الفوتر يظهر فقط في هذه الصفحة
    }
    return render(request, 'employees/ats_list.html', context)



@login_required
def delete_ats(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    messages.success(request, "✅ تم حذف الموظف بنجاح.")
    return redirect('list_ats')


@login_required
def fonctionnaire_detail(request, pk):
    fonctionnaire = get_object_or_404(Fonctionnaire, pk=pk)
    return render(request, 'employees/fonctionnaire_detail.html', {'fonctionnaire': fonctionnaire})


# ============ Mise à jour ============
from .forms import PaieForm, PrimeForm, CongeForm

# ---- Ajouter ou modifier la Paie ----
@login_required
def update_paie(request, pk):
    fonctionnaire = get_object_or_404(Fonctionnaire, pk=pk)
    if request.method == 'POST':
        form = PaieForm(request.POST)
        if form.is_valid():
            paie = form.save(commit=False)
            paie.fonctionnaire = fonctionnaire
            paie.save()
            return redirect('fonctionnaire_detail', pk=pk)
    else:
        form = PaieForm()
    return render(request, 'employees/upprint/update_paie.html', {'form': form, 'fonctionnaire': fonctionnaire})


# ---- Ajouter une Prime ----
@login_required
def update_prime(request, pk):
    fonctionnaire = get_object_or_404(Fonctionnaire, pk=pk)
    if request.method == 'POST':
        form = PrimeForm(request.POST)
        if form.is_valid():
            prime = form.save(commit=False)
            prime.fonctionnaire = fonctionnaire
            prime.save()
            return redirect('fonctionnaire_detail', pk=pk)
    else:
        form = PrimeForm()
    return render(request, 'employees/upprint/update_prime.html', {'form': form, 'fonctionnaire': fonctionnaire})


# ---- Ajouter un Congé ----
@login_required
def update_conge(request, pk):
    fonctionnaire = get_object_or_404(Fonctionnaire, pk=pk)
    if request.method == 'POST':
        form = CongeForm(request.POST)
        if form.is_valid():
            conge = form.save(commit=False)
            conge.fonctionnaire = fonctionnaire
            conge.save()
            return redirect('fonctionnaire_detail', pk=pk)
    else:
        form = CongeForm()
    return render(request, 'employees/upprint/update_conge.html', {'form': form, 'fonctionnaire': fonctionnaire})





# 🔹 Modifier ou ajouter une promotion
@login_required
def update_promotion(request, pk):
    fonctionnaire = get_object_or_404(Fonctionnaire, pk=pk)
    promotion, created = Promotion.objects.get_or_create(fonctionnaire=fonctionnaire)

    if request.method == 'POST':
        form = PromotionForm(request.POST, instance=promotion)
        if form.is_valid():
            form.save()
            return redirect('fonctionnaire_detail', pk=fonctionnaire.pk)
    else:
        form = PromotionForm(instance=promotion)

    return render(request, 'employees/upprint/update_promotion.html', {
        'form': form,
        'fonctionnaire': fonctionnaire,
        'title': 'Update Promotion',
    })


# 🔹 Modifier ou ajouter un échelon
@login_required
def update_echelon(request, pk):
    fonctionnaire = get_object_or_404(Fonctionnaire, pk=pk)
    echelon, created = Echelon.objects.get_or_create(fonctionnaire=fonctionnaire)

    if request.method == 'POST':
        form = EchelonForm(request.POST, instance=echelon)
        if form.is_valid():
            form.save()
            return redirect('fonctionnaire_detail', pk=fonctionnaire.pk)
    else:
        form = EchelonForm(instance=echelon)

    return render(request, 'employees/upprint/update_echelon.html', {
        'form': form,
        'fonctionnaire': fonctionnaire,
        'title': 'Update Echelon',
    })


# 🔹 Afficher l’historique du fonctionnaire
@login_required
def view_historique(request, pk):
    fonctionnaire = get_object_or_404(Fonctionnaire, pk=pk)
    historique = Historique.objects.filter(fonctionnaire=fonctionnaire).order_by('-date_action')

    return render(request, 'employees/upprint/view_historique.html', {
        'fonctionnaire': fonctionnaire,
        'historique': historique,
        'title': 'Historique des actions',
    })







# ============ Imprimer ============
@login_required
def print_fiche_paie(request, pk):
    fonctionnaire = get_object_or_404(Fonctionnaire, pk=pk)
    paie = Paie.objects.filter(fonctionnaire=fonctionnaire).last()  # آخر راتب مسجل

    context = {
        'fonctionnaire': fonctionnaire,
        'paie': paie,
    }

    return render(request, 'employees/upprint/print_fiche_paie.html', context)

@login_required
def print_attestation_travail(request, pk):
    fonctionnaire = get_object_or_404(Fonctionnaire, pk=pk)
    return render(request, 'employees/upprint/print_attestation_travail.html', {'fonctionnaire': fonctionnaire})




def print_titre_conge(request, pk):
    fonctionnaire = get_object_or_404(Fonctionnaire, pk=pk)

    conge = Conge.objects.filter(fonctionnaire=fonctionnaire).order_by('-id').first()

    if not conge:
        messages.warning(request, "⚠️ No leave record found for this employee.")
        return HttpResponseRedirect(reverse('fonctionnaires_detail', args=[pk]))

    if not all([conge.type_conge, conge.date_debut, conge.date_fin, conge.motif]):
        messages.error(request, "⚠️ Leave data is incomplete. Please check the form first.")
        return HttpResponseRedirect(reverse('fonctionnaires_list'))

    return render(request, 'employees/upprint/print_titre_conge.html', {'conge': conge})