from django.db import models


class Resume(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(
        max_length=3, choices={"m": "Male", "f": "Female", "o": "Others"}
    )
    nationality = models.CharField(max_length=100)
    division = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.PositiveIntegerField()
    job_location = models.CharField(max_length=100)
    mobile = models.PositiveIntegerField()
    email = models.EmailField()
    profile_photo = models.ImageField(upload_to="images", blank=True)
    resume_file = models.FileField(upload_to="documents", blank=True)
