from django.conf import settings
from django.shortcuts import render, redirect
from .models import Banner,About,Services,Services_details,Mission,Gallery
from django.shortcuts import render,get_object_or_404
from .models import Testimonial
from .forms import TestimonialForm,contactForm
from .forms import CareerForm
from django.contrib import messages



# Create your views here.
def BASE(request):
    service = Services.objects.all()

    context = {
        'service': service
    }


    return render(request,'base.html',context)


def INDEX(request):
    banner=Banner.objects.all()
    about = About.objects.first()
    service=Services.objects.all()

    context={
        'banner':banner,
        'about' :about,
        'service':service
    }
    return render(request,'index.html',context)


def SERVICES(request):
    service = Services.objects.all()

    context = {
        'service': service
    }

    return render(request,'services.html',context)



def SERVICES_DETAILS(request,id):
    service = Services.objects.all()


    obj = get_object_or_404(Services, pk=id)
    details = get_object_or_404(Services_details, pk=id)

    context={
        'obj':obj,
        'details':details,
        'service': service
    }




    return render(request,'services_details.html',context)


def ABOUT(request):

    mission = Mission.objects.first()
    about = About.objects.first()



    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            designation = form.cleaned_data['designation']
            message = form.cleaned_data['message']
            Testimonial.objects.create(name=name, designation=designation, message=message)
            return redirect('index')
    else:
        form = TestimonialForm()
    testimonials = Testimonial.objects.all().order_by('-created_at')
    context = {'form': form, 'testimonials': testimonials,'about': about,'mission': mission,}




    return render(request, 'about.html', context)


def CAREER(request):
    if request.method == 'POST':
        form = CareerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submitted successfully.')
            return redirect('success')
    else:
        form = CareerForm()
    return render(request, 'career.html', {'form': form})

def success(request):
    return render(request, 'success.html')





def CONTACT(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    else:
        form = contactForm()
    return render(request, 'contact.html', {'form': form})


def GALLERY(request):
    gallery = Gallery.objects.all()

    context={
        'gallery':gallery
    }
    return render(request,'gallery.html',context)