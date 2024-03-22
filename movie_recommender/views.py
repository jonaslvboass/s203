from django.shortcuts import render
from .models import CustomUser

def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'user_list.html', {'users': users})

def create_users(request):
    # Criando alguns usuários de exemplo
    CustomUser.objects.create(username='user1', email='user1@example.com')
    CustomUser.objects.create(username='user2', email='user2@example.com')
    CustomUser.objects.create(username='user3', email='user3@example.com')
    return render(request, 'user_created.html')
