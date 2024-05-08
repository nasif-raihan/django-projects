from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

GROUP_CHOICES = {"science": "Science", "commerce": "Commerce", "arts": "Humanities"}
GRADE_CHOICES = {
    "excellent": "Excellent",
    "good": "Good",
    "average": "Average",
    "poor": "Poor",
}


class Subject(models.Model):
    name = models.CharField(max_length=100)
    credit = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=[
            MaxValueValidator(limit_value=25),
            MinValueValidator(limit_value=0.25),
        ],
    )

    def __str__(self) -> str:
        return f"{self.name}"


class Grade(models.Model):
    remark = models.CharField(max_length=15, choices=GRADE_CHOICES)

    def __str__(self) -> str:
        return f"{self.remark}"


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.ForeignKey(to=Subject, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name}"


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    group = models.CharField(max_length=15, choices=GROUP_CHOICES)
    teacher = models.ManyToManyField(to=Teacher)

    def __str__(self) -> str:
        return f"{self.name}"


class MarkSheet(models.Model):
    student = models.ForeignKey(to=Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(to=Subject, on_delete=models.CASCADE)
    grade = models.ForeignKey(to=Grade, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.subject.name}"
