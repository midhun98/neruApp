from django.contrib import admin
from . import models
# Register your models here.


admin.site.register(models.Advertiser)
admin.site.register(models.Location)
admin.site.register(models.Ad)
admin.site.register(models.Transaction)
