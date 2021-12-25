from django.contrib import admin
from .models import App, Plan, Subscription

admin.site.register(App)
admin.site.register(Subscription)
admin.site.register(Plan)

# Register your models here.
