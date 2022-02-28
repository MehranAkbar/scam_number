from django.contrib import admin
from .models import phonemodel, reviewmodel

# Register your models here.
admin.site.register(phonemodel)
admin.site.register(reviewmodel)