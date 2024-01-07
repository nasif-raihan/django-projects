from django.shortcuts import render
from .forms import ResumeForm
from .models import Resume
from django.views import View


class HomeView(View):
    def get(self, request):
        form = ResumeForm()
        return render(request, "uploader/home.html", {"form": form})

    def post(self, request):
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return render(request, "uploader/home.html", context={"form": form})
