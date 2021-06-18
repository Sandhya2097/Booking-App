from django.urls import path
from .import views
from django.contrib.auth.views import LoginView

urlpatterns = [
     path('',views.register,name="register"),
     path('dashboard/',views.dashboard,name='dashboard'),
     path('login/',LoginView.as_view(),name="login_url"),
     path('logout/',views.logout,name="logout"),
 ]