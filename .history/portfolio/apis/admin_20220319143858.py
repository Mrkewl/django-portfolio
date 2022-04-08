from django.contrib import admin

# Register your models here.
from .models.project import Project
from .models.user import User

admin.site.register(Project)
admin.site.register(User)
