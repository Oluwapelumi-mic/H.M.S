from django.urls import path
from .views import About , Home , Contact , Login ,Logout_admin , Logout

urlpatterns = [
    path('', Home , name='home'),
    path('about/', About , name='about'),
    path('contact/', Contact , name='contact'),
    path('lO/', Logout , name='Logout'),
    path('admin_login/', Login, name='login'),
    path('Logout/', Logout_admin, name='logout'),
] 