from django.shortcuts import render, HttpResponse


def Homepage(request):
    return render(request, "homepage.html")


def Contacts(request):
    return HttpResponse('Contacts')


def About_Us(request):
    return HttpResponse('About Us')


