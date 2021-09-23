from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from accounts.models import UserAccount


class UserAccountInline(admin.StackedInline):
    model = UserAccount
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = (UserAccountInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
