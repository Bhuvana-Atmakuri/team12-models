from django.contrib import admin

# Register your models here.
from .models import Hotels,items
from .models import *

admin.site.register(Hotels)
admin.site.register(items)
admin.site.register(Cart)
admin.site.register(Dinein)
admin.site.register(dine1)