from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Store)
admin.site.register(Adress)
admin.site.register(StoreReview)

admin.site.register(StoreImage)
