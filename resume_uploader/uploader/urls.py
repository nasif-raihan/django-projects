from django.urls import path

from uploader.views import HomeView

urlpatterns = [path("", HomeView.as_view())]
