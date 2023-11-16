from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Case

from .models import My_User,Police

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_filter=["username"]
    search_fields=["first_name"]
    list_per_page=10

admin.site.register(My_User,UserAdmin)
admin.site.register(Police)
admin.site.register(Case)
