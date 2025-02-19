from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('userlogin/', views.user_login, name='userlogin'),
    path('adminlogin/', views.admin_login, name='adminlogin'),
    path('adminloginNext/', views.admin_login_next, name='adminloginNext'),  
    path('userhome/', views.user_home, name='userhome'),
    path('adminhome/', views.admin_home, name='adminhome'),
    path('logout/', views.logout_view, name='logout'),
    path('adminviewusers/', views.admin_view_users, name='adminviewusers'),
    path('adminviewfaq/', views.admin_view_faq, name='adminviewfaq'),  
    path('addfaq/', views.add_faq, name='addfaq'), 
    path('logout/', views.logout_view, name='logout'), 
    path('segmentation/', views.segmentation, name='segmentation'),
    path('userviewfaq/', views.user_view_faq, name='userviewfaq'), 
    path('segmentationresults/',views.segmentationresults, name='segmentationresults'),
]




