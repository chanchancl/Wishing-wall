from django.contrib import admin

# Register your models here.
from .models import Wishing,ServerData

admin.site.register(ServerData)
admin.site.register(Wishing)
