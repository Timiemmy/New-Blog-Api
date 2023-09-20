from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User
from .forms import UserCreateForm, UserChangeForm

@admin.register(User)
class UserAccountAdmin(UserAdmin):
    add_form = UserCreateForm
    form = UserChangeForm
    model = User
    list_display = ["email", "username", "name", "is_staff",]
    fieldsets = UserAdmin.fieldsets +((None, {"fields":("name",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("name",)}),)


# admin.site.register(UserCreateForm)
# admin.site.register(UserChangeForm)