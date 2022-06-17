from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import *
from django.urls import reverse


def create(request):
    if request.method == "POST":
        Student.objects.create(
        name =request.POST["name"],
        marks = request.POST["marks"],
        mobile = request.POST["mobile"],
        )
        return HttpResponseRedirect('/menu/menu_list/')
        # return HttpResponseRedirect(reverse('menu:menu_list'))
    return render(request, "menu/third.html")