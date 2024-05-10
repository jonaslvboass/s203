from django.contrib import admin
from .models import Movie, Myrating, MyList,FollowList

# Register your models here.
admin.site.register(Movie)
admin.site.register(Myrating)
admin.site.register(MyList)
admin.site.register(FollowList)