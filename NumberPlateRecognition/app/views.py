from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

from app.Lib import sv
import os
from django.conf import settings
from .forms import ImageForm

# Create your views here.
def index(request):
    context = {}
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = request.FILES['image']
            image.name = 't.png'
            fullname = os.path.join(settings.MEDIA_ROOT, image.name)
            if os.path.exists(fullname):
                os.remove(fullname)
            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            output = sv.main()
            context['success'] = output
    else:
        form = ImageForm()

    context['form'] = form
    return render(request, 'app/index.html', context)
