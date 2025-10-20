from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # توجيه المستخدم حسب الدور (role)
            if user.role == "Admin":
                return redirect("admin_dashboard")
            elif user.role == "Employé":
                return redirect("employee_dashboard")
            else:
                return redirect("employee_dashboard")
                return redirect("")
        else:
            messages.error(request, "اسم المستخدم أو كلمة المرور غير صحيحة.")
    
    return render(request, "accounts/login.html")


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')



def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Compte créé avec succès ! Vous pouvez maintenant vous connecter.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def admin_dashboard(request):
    return render(request, "accounts/admin_dashboard.html")

@login_required
def employee_dashboard(request):
    return render(request, "accounts/employee_dashboard.html")

def logout_view(request):
    logout(request)
    return redirect("login")
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages

@login_required
def edit_account(request):
    user = request.user

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')

        user.username = username
        user.email = email
        user.save()

        messages.success(request, 'Compte mis à jour avec succès ✅')
        return redirect('dashboard')  # أو أي صفحة تريد العودة إليها بعد التعديل

    context = {'user': user}
    return render(request, 'accounts/edit_account.html', context)



