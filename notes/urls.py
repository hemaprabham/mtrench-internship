from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('user/', views.user, name='user'),
    path('logouts/', views.logouts, name='logouts'),
    path('profile/',views.editprofile,name='profile'),
    path('profilee/',views.profilee,name='profilee'),
    path('uploaddash/',views.uploaddash,name='uploaddash'),
    path('upload/',views.upload,name='upload'),
    path('edit/<int:pk>/',views.pdfedit,name='edit'),
    path('delete/<int:pk>/',views.delete,name='delete'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
