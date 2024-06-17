from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('genre/', views.index_genre, name='indexgenre'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('<int:movie_id>/', views.detail, name='detail'),
    path('watch/', views.watch, name='watch'),
    path('users/', views.list_users, name='list_users'),
    path('users/<str:id>', views.user_detail, name='user_detail'),
    ]