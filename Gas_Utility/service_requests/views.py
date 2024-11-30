from django.shortcuts import render, get_object_or_404
from .models import ServiceRequest
from .forms import ServiceRequestForm

def home(request):
    return render(request, 'service_requests/home.html')

def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'service_requests/thanks.html')
    else:
        form = ServiceRequestForm()
    return render(request, 'service_requests/submit_request.html', {'form': form})

def track_request(request, request_id):
    request_obj = get_object_or_404(ServiceRequest, id=request_id)
    return render(request, 'service_requests/track_request.html', {'request': request_obj})

def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            new_request = form.save()
            return render(request, 'service_requests/thanks.html', {'request_id': new_request.id})
    else:
        form = ServiceRequestForm()
    return render(request, 'service_requests/submit_request.html', {'form': form})
