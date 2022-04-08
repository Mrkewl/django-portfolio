from django.contrib import admin

# Register your models here.
from .models.project import Project
from .models.user import User
from .models.design import Design

admin.site.register(Project)
admin.site.register(User)
admin.site.register(Design)
