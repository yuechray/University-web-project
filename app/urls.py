from django.urls import path
from . import views  

urlpatterns = [
    path('', views.main, name='main'), 
    path('news/', views.news, name='news'),     
    path('about/', views.about, name='about'),  
    path('links/', views.links, name='links'),
    path('pool/', views.pool, name='pool'),
    path('create', views.create, name='create'),
    path('login', views.login_view, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout_, name='logout'),
    path('detail/<int:pk>/', views.detail, name='detail_news'),
    path('admin/', views.admin, name="admin"),
    path('update/<int:pk>/', views.update_news, name='update_news'),
    path('delete_news/<int:pk>/', views.delete_news, name='delete_news'),
    path('video/', views.videopost, name='videopost'),
]