from django.contrib import admin
from DBModelApp.models import Employee
# Register your models here.
class emAdmin(admin.ModelAdmin):
    list_display = ['eno','ename','esal','eaddr']

admin.site.register(Employee,emAdmin)

from DBModelApp.models import Company
class compadmin(admin.ModelAdmin):
    list_display = ['compid','compname','noofemps','compaddr','compshare']

admin.site.register(Company,compadmin)