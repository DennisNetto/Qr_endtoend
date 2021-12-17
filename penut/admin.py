from django.contrib import admin
from .models import TokenStorage, HumanStorage
# Register your models here.
admin.site.register(TokenStorage)
admin.site.register(HumanStorage)

