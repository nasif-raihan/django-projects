from django.urls import path

from uploader.views import HomeView, CandidateView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("<int:pk>", CandidateView.as_view(), name="candidate"),
]
