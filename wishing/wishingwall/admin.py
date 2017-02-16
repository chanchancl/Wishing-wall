from django.contrib import admin

# Register your models here.
from .models import Wishing,ServerData,VisitData

admin.site.register(ServerData)
admin.site.register(Wishing)
admin.site.register(VisitData)