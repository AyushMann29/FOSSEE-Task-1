# Django Imports
from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings

# Local Imports
from cms.models import Page


def index(request):
    # Always redirect to /workshop/status
    return redirect('/workshop/status')
