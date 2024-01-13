from django import forms

from .models import Resume


class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(
        choices={"Male": "Male", "Female": "Female", "Others": "Prefer not to say"},
        widget=forms.RadioSelect,
    )
    job_location = forms.MultipleChoiceField(
        label="Preferred Job Location",
        choices={
            "Barishal": "Barishal",
            "Dhaka": "Dhaka",
            "Khulna": "Khulna",
            "Sylhet": "Sylhet",
            "Remote": "Remote",
        },
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Resume
        fields = "__all__"
        labels = {
            "name": "Name",
            "birth_date": "Birth Date",
            "gender": "Sex",
            "nationality": "Nationality",
            "division": "Division",
            "city": "City",
            "postal_code": "Post Code",
            "mobile": "Mobile Number",
            "email": "Email Address",
            "profile_photo": "Profile Image",
            "resume_file": "Document",
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "birth_date": forms.DateInput(
                attrs={"class": "form-control", "id": "datePicker"}
            ),
            "nationality": forms.TextInput(attrs={"class": "form-control"}),
            "division": forms.TextInput(attrs={"class": "form-control"}),
            "city": forms.TextInput(attrs={"class": "form-control"}),
            "postal_code": forms.NumberInput(attrs={"class": "form-control"}),
            "mobile": forms.NumberInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
        }
