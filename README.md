# 🧾 ESTN HRMS — Human Resource Management System

**ESTN HRMS** is a web-based Human Resource Management System built with **Django**.  
It provides a centralized platform to manage employees, payroll, attendance, and HR operations efficiently.

---

## 🚀 Features

### 👥 Employee Management
- Add, edit, and delete employee profiles.
- Manage departments, job titles, and designations.
- Upload and store employee documents.

### 💰 Payroll Management
- Manage salaries, allowances, and deductions.
- Automatically generate monthly payslips.
- Export or print payroll reports.

### 🕒 Attendance & Leave
- Track employee attendance and leaves.
- Manage leave requests and approvals.

### 📂 Document Management
- Upload, categorize, and manage HR documents securely.

### 🔐 Authentication & Authorization
- Role-based access (Admin, HR, Employee).
- Secure authentication using Django’s built-in system.

---

## 🧩 Project Structure

estin_hrms/
│
├── accounts/ # User accounts and authentication
├── core/ # Core settings and configuration
├── documents/ # Employee documents and uploads
├── employees/ # Employee management
├── hr/ # HR functionalities
├── payroll/ # Payroll and salary management
├── static/ # CSS, JS, and image files
├── templates/ # HTML templates
├── manage.py # Django management script
└── requirements.txt # Project dependencies

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Youssefblj/estin_hrms.git
cd estin_hrms
2️⃣ Create and activate virtual environment
bash
Copy code
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
3️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Apply migrations
bash
Copy code
python manage.py makemigrations
python manage.py migrate
5️⃣ Create superuser
bash
Copy code
python manage.py createsuperuser
6️⃣ Run the development server
bash
Copy code
python manage.py runserver
Open your browser and go to 👉 http://127.0.0.1:8000/

🧠 Tech Stack
Backend: Django

Frontend: HTML, CSS, Bootstrap

Database: SQLite (default) or PostgreSQL

Language: Python 3.x

🧑‍💻 Author
Youssef B.
💼 Software Developer — ESTN
🔗 GitHub Profile

📝 License
This project is open-source and available under the MIT License.

⭐ If you found this project helpful, consider giving it a star!

yaml
Copy code

---

✅ You can now:
1. Go to your GitHub repo (`estin_hrms`),
2. Click **Add file → Create new file** (or edit existing `README.md`),
3. Paste all this code,
4. Commit changes.

It’ll display perfectly with GitHub markdown formatting.
