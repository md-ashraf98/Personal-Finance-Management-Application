from django import forms
from .models import User
from django.core.exceptions import ValidationError
import re

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, min_length=8)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['full_name', 'contact_number', 'email', 'username', 'password']

    def clean_password(self):
        password = self.cleaned_data.get('password')
        # Password should include 1 uppercase, 1 lowercase, 1 digit, and 1 special character
        pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
        if not re.match(pattern, password):
            raise ValidationError(
                "Password must contain at least 8 characters, including one uppercase letter, one lowercase letter, one number, and one special character."
            )
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            self.add_error("confirm_password", "Passwords do not match.")
        return cleaned_data


class SignInForm(forms.Form):
    username_or_phone = forms.CharField(label="Username or Phone Number", max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, label="Password")

    def clean_username_or_phone(self):
        username_or_phone = self.cleaned_data.get('username_or_phone')
        if not username_or_phone:
            raise ValidationError("This field is required.")
        # Check if it's a phone number or username
        if username_or_phone.isdigit():
            # If it's a phone number, check if it's in valid format (optional validation)
            if len(username_or_phone) != 10:  # Example: For a 10-digit phone number
                raise ValidationError("Enter a valid 10-digit phone number.")
        else:
            # Username is not empty and valid
            return username_or_phone

        return username_or_phone

from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['type', 'category', 'amount', 'date', 'description']

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class EditTransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['type', 'category', 'amount', 'date', 'description']

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
