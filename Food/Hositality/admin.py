from django.contrib import admin

# Register your models here.
from .models import Hotels,items,Customer
admin.site.register(Hotels)
admin.site.register(items)
admin.site.register(Customer)