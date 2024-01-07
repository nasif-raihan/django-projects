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
    return render(
        request, "uploader/home.html", context={"form": form, "title": "uploader"}
    )


def show_images(request):
    images = Image.objects.all()
    form = ImageForm()
    return render(
        request,
        "uploader/home.html",
        context={"title": "uploader", "form": form, "images": images},
    )
