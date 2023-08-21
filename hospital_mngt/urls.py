from django.urls import path
from .views import About , Home , Contact ,Index, Login ,Logout_admin , Logout, View_Doctor,Delete_Doctor, Add_Doctor ,Add_Patient ,Delete_Patient, View_Patient , View_Appointment ,Add_Appointment ,Delete_Appointment

urlpatterns = [
    path('', Home , name='home'),
    path('about/', About , name='about'),
    path('contact/', Contact , name='contact'),
    path('dashboard/', Index , name='dashboard'),
    path('lO/', Logout , name='Logout'),
    path('admin_login/', Login, name='login'),
    path('Logout/', Logout_admin, name='logout'),
    path('view_doctor/', View_Doctor, name='view_doctor'),
    path('add_doctor/', Add_Doctor, name='add_doctor'),
    path('delete_doctor(?p<int:pid>)/', Delete_Doctor, name='delete_doctor'),
    path('view_patient/', View_Patient, name='view_patient'),
    path('add_patient/', Add_Patient, name='add_patient'),
    path('delete_patient(?p<int:pid>)/', Delete_Patient, name='delete_patient'),
    path('view_appointment/', View_Appointment, name='view_appointment'),
    path('add_appointment/', Add_Appointment, name='add_appointment'),
    path('delete_appointment(?p<int:pid>)/', Delete_Appointment, name='delete_appointment'),
] 