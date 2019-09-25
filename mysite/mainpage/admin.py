from django.contrib import admin
from .models import user_service,user_issue

# Register your models here.
admin.site.register(user_service)
admin.site.register(user_issue)
