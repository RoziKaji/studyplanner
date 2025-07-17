from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse

def log_in(request):
    if request.method == "POST":
        email = request.POST ["email"]
        password = request.POST ["password"]
        user = authenticate(request, username= email, password = password)
        if user is None:
            print("ekfhekhfkehfkrwhk")
        else:
            login(request, user)
            return HttpResponseRedirect(reverse("planner:subject_list"))            
    return render(request, "login.html")
