from django.contrib import admin

from .models import User, Movies, Actors, Directors,Trend

# Register your models here.
admin.site.register(Movies)
admin.site.register(User)
admin.site.register(Actors)
admin.site.register(Directors)
admin.site.register(Trend)
