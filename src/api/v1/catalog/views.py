from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

def vote(request) -> HttpResponse:
    return HttpResponse("hello")