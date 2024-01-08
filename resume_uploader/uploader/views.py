from django.shortcuts import render
from django.views import View

from .forms import ResumeForm
from .models import Resume


class HomeView(View):
    @staticmethod
    def get(request):
        form = ResumeForm()
        candidates = Resume.objects.all()
        return render(
            request, "uploader/home.html", {"form": form, "candidates": candidates}
        )

    @staticmethod
    def post(request):
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return render(request, "uploader/home.html", {"form": form})


class CandidateView(View):
    @staticmethod
    def get(request, pk):
        candidate = Resume.objects.get(id=pk)
        return render(request, "uploader/candidate.html", {"candidate": candidate})
