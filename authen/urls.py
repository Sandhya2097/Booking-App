from django.urls import path
from .import views
from django.contrib.auth.views import LoginView

urlpatterns = [
     path('',views.register,name="register"),
     path('login/',LoginView.as_view(),name="login_url"),
     path('dashboard/',views.dashboard,name='dashboard'),
     path('movies/',views.movies,name="movies"),
     path('logout/',views.logout,name="logout"),
 ]