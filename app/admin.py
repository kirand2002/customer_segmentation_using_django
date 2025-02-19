from django.contrib import admin

from .models import AdminLogin,Signup,FAQ




admin.site.register(Signup),
admin.site.register(FAQ),
admin.site.register(AdminLogin),



# Register your models here.


