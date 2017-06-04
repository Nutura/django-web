# -*- coding: utf-8 -*-
from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render
import os
import subprocess


work_dir = os.path.dirname(os.path.realpath(__file__))

def index(request):
  if request.method == 'POST':
    image_path = os.path.join(work_dir, 'uploads', request.FILES['source'].name)
    with open(image_path, 'wb+') as destination:
        for chunk in request.FILES['source'].chunks():
            destination.write(chunk)


    ocr_executable = os.path.join(work_dir, '../../georgian-ocr-v2/bin/ocr.sh')
    export_executable = os.path.join(work_dir, '../../georgian-ocr-v2/bin/export_words.sh')

    print "image path is" , image_path
    subprocess.check_output([ocr_executable, image_path])
    recognized_text = subprocess.check_output([export_executable, image_path])


    return render(request, 'webapp/home.html', {
      'recognized_text': recognized_text
      })
  else:
    return render(request, 'webapp/home.html')
