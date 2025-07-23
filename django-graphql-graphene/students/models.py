from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    category = models.CharField(
        choices={
            "junior": "junior",
            "intermediate": "intermediate",
            "senior": "senior",
        },
        default="junior",
    )

    def __str__(self):
        return f"{self.email}"
