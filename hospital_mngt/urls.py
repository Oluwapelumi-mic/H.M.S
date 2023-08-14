from django.urls import path
from .views import About , Home , Contact , Login ,Logout_admin , Logout, View_Doctor,Delete_Doctor, Add_Doctor

urlpatterns = [
    path('', Home , name='home'),
    path('about/', About , name='about'),
    path('contact/', Contact , name='contact'),
    path('lO/', Logout , name='Logout'),
    path('admin_login/', Login, name='login'),
    path('Logout/', Logout_admin, name='logout'),
    path('view_doctor/', View_Doctor, name='view_doctor'),
    path('add_doctor/', Add_Doctor, name='add_doctor'),
    path('delete_doctor(?p<int:pid>)/', Delete_Doctor, name='delete_doctor'),
] 