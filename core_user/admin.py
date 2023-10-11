from django.contrib import admin
from core_user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
