from django.shortcuts import render,redirect
from requests import request
from .models import Project
def home(request):
    return render(request,'home.html')

def services(request):
    return render(request,"services.html")

def projects(request):
    projects = Project.objects.filter(completed=True)
    return render(request, 'projects.html', {'projects': projects})



from django.shortcuts import render, redirect
from .models import Consultation, Estimate

def contact_view(request):
    if request.method == "POST":

        # CONSULTATION FORM
        if 'message' in request.POST:
            Consultation.objects.create(
                name=request.POST.get('name'),
                phone=request.POST.get('phone'),
                email=request.POST.get('email'),
                message=request.POST.get('message')
            )
            return redirect('thank_you')

        # ESTIMATE FORM
        if 'service' in request.POST:
            Estimate.objects.create(
                name=request.POST.get('name'),
                phone=request.POST.get('phone'),
                service=request.POST.get('service'),
                location=request.POST.get('location'),
                details=request.POST.get('details')
            )
            return redirect('thank_you')

    return render(request, 'contact.html')


def thank_you(request):
    return render(request, 'thank_you.html')


