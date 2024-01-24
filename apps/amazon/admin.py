from django.contrib import admin
from .models import Order, Dispute, Return

# Register your models here.

admin.site.register(Order)
admin.site.register(Dispute)
admin.site.register(Return)
