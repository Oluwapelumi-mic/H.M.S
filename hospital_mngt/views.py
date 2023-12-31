from django.contrib.auth.models import User
from django.shortcuts import redirect, render , redirect
from django.contrib.auth import authenticate, login, logout
from .models import Doctor, Patient , Appointment
# Create your views here.
def About(request):
    return render(request,'about.html' )

def Home(request):
    return render(request, 'home.html')

def Contact(request):
    return render(request, 'contact.html')



def Logout(request):
    return render(request, 'base.html')

def Index(request):
    if not request.user.is_staff:
        return redirect ('login')
    return render(request, 'base.html')

def Login(request):
    error = ""
    if request.method =="POST":
        u = request.POST['adminName']
        p = request.POST['password']
        user = authenticate(username= u, password=p)
        try:
            if user.is_staff:
                login(request,user)
                error = "no"

            else:
                error = "yes"

        except:
            error = "yes"
    d = {'error':error}
    return render(request, 'login.html', d)

def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')

def View_Doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Doctor.objects.all()
    d ={'doc': doc }
    return render(request, 'view_doctor.html', d)


def Delete_Doctor(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    doctor = Doctor.objects.get(id =pid)
    doctor.delete()
    return redirect('view_doctor')



def Add_Doctor(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method =="POST":
        n = request.POST['name']
        g = request.POST['gender']
        e = request.POST['email']
        m = request.POST['mobile_no']
        sp = request.POST['speciality']
        try:
            Doctor.objects.create(name=n, gender=g,mobile_no=m,speciality=sp, email=e)
            error = "no"
        except Exception as e:
            error = "yes"
            print(e)

    d = {"error": error}
    return render(request, 'add_doctor.html', d)


def View_Patient(request):
    if not request.user.is_staff:
        return redirect('login')
    pat = Patient.objects.all()
    d ={'pat': pat }
    return render(request, 'view_patient.html', d)


def Delete_Patient(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.get(id =pid)
    patient.delete()
    return redirect('view_patient')



def Add_Patient(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method =="POST":
        nm = request.POST['pname']
        gd = request.POST['pgender']
        mn = request.POST['pmobile_no']
        a = request.POST['paddress']
        try:
            Patient.objects.create(pname=nm, pgender=gd,pmobile_no=mn,paddress=a)
            error = "no"
        except:
            error = "yes"

    p = {"error": error}
    return render(request, 'add_patient.html', p)

def View_Appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    apt = Appointment.objects.all()
    a ={'apt': apt }
    return render(request, 'view_appointments.html', a)


def Delete_Appointment(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    appointment = Appointment.objects.get(id =pid)
    appointment.delete()
    return redirect('view_appointments')



def Add_Appointment(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()
    if request.method =="POST":
        dc = request.POST['doctor']
        p = request.POST['patient']
        d = request.POST['date']
        t = request.POST['time']
        doctor = Doctor.objects.filter(name=dc).first()
        patient = Patient.objects.filter(pname=p).first()
        try:
            Appointment.objects.create(doctor=doctor, date=d,time=t,patient=patient)
            error = "no"
        except:
            error = "yes"

    a = {"error": error ,"doctor": doctor1 ,"patient":patient1}
    return render(request, 'add_appointment.html', a)

def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    
    doctor_count = Doctor.objects.count()
    patient_count = Patient.objects.count()
    appointment_count = Appointment.objects.count()

    context = {
        'doctor_count': doctor_count,
        'patient_count': patient_count,
        'appointment_count': appointment_count
    }

    return render(request, 'base.html', context)
                