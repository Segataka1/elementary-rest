from django.contrib import admin
from acounts.models import UserAdmin, UserClient, User

admin.site.register(User)
admin.site.register(UserClient)
admin.site.register(UserAdmin)