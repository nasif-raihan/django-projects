from django.shortcuts import render

from .forms import ImageForm
from .models import Image


def home(request):
    return render(request, "base.html", context={"title": "base"})


def upload_image(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    images = Image.objects.all()
    return render(
        request,
        "uploader/home.html",
        context={"form": form, "title": "uploader", "images": images},
    )
