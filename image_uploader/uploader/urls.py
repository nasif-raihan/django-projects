from django.urls import path

from .views import home, upload_image

urlpatterns = [path("", home), path("upload", upload_image, name="upload")]
