from django.db.models.query import RawQuerySet
from .models import App, Plan, Subscription
from django.views.generic import CreateView, UpdateView, DetailView, ListView
from django.shortcuts import render


def home(request):
    
    apps = App.objects.filter(user=request.user.id)
    context = {"apps": apps}
    return render(request, "home/index.html", context)
