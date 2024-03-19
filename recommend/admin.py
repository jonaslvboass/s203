from django.contrib import admin
from .models import Movie, Myrating, MyList

# Here you'll register your models
admin.site.register(Movie)
admin.site.register(Myrating)
admin.site.register(MyList)