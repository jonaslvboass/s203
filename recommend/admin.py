from django.contrib import admin
from .models import Movie, MyRating, MyList,FollowList

# Register your models here.
admin.site.register(Movie)
admin.site.register(MyRating)
admin.site.register(MyList)
admin.site.register(FollowList)