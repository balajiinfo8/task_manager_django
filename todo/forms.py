
from django import forms
from .models import Todo
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model();


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "details"]


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username","email")
    def clean_email(self):
        email = self.cleaned_data["email"].strip();

        # condition check mail address
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                "An Account with this email Already Exits."
            );
        return email

