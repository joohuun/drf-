from django.contrib import admin
from .models import Hobby, Profile, User

# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Hobby)

