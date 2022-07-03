from django.contrib import admin
from .models import Profile,BlogPost,Comment
# Register your models here.
admin.site.register(BlogPost)
admin.site.register(Profile)
admin.site.register(Comment)