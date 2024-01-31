from django.contrib import admin

from .models import Case, CustomUser,Notification


# Register your models here.
# class UserAdmin(admin.ModelAdmin):
#     list_filter= ["username"]
#     search_fields= ["first_name"]
#     list_per_page= 10
# admin.site.register(UserAdmin)

# class UserDetails(admin.ModelAdmin):
#     fieldsets=[
#         (None,{'fields':['username','email']}),
#         ('more information',{'fields':['phone','first_name']})
#     ]
#     # list_display=['username','email']
#     list_filter=['type']
#     search_fields=['username']
#     list_per_page=10
#

admin.site.register(Case)
admin.site.register(CustomUser)
admin.site.register(Notification)

admin.site.site_header= 'Cops Project'