# -*- coding: utf-8 -*-
from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render


from .forms import UploadFileForm

# Imaginary function to handle an uploaded file.
from .forms import handle_uploaded_file

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

# Create your views here.

def index(request):
	return render(request, 'webapp/home.html')


