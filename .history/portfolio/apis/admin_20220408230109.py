from django.contrib import admin
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin

# Register your models here.
from .models.project import Project
from .models.user import User
from .models.design import Design

admin.site.register(Project)
admin.site.register(User)
admin.site.register(Design)
