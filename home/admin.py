from django.contrib import admin
from .models import App, Plans, Subscriptions

admin.site.register(App)
admin.site.register(Subscriptions)
admin.site.register(Plans)

# Register your models here.
