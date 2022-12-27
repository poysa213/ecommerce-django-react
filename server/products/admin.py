from django.contrib import admin
from . import models
# Register your models here.


admin.site.register(models.Category)
admin.site.register(models.Promotion)
admin.site.register(models.Product)
admin.site.register(models.ProductImage)