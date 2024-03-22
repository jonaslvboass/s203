from django.shortcuts import render
from django.views.generic.list import ListView

from .models import User

class UserListView(ListView):
    model = User
    template_name = "users/index.html"
    context_object_name = "all_users"

    def get_queryset(self):
        return User.objects.all()
