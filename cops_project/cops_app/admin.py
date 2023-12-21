from django.contrib import admin

from .models import Case, CustomUser,Notification


# Register your models here.
# class UserAdmin(admin.ModelAdmin):
#     list_filter= ["username"]
#     search_fields= ["first_name"]
#     list_per_page= 10
# admin.site.register(UserAdmin)
admin.site.register(Case)
admin.site.register(CustomUser)
admin.site.register(Notification)

