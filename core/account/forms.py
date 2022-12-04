from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from account.models import User


class UserLoginForm(forms.Form):
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'placeholder': 'password'}))
    username = forms.CharField(label='username', widget=forms.TextInput(attrs={'placeholder': 'ایمیل یا نام کاربری'}))

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserRegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'username')

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'type': 'email', 'placeholder': 'ادرس ایمیل'})
        self.fields['username'].widget.attrs.update({'type': 'text', 'placeholder': 'نام کاربری'})
        self.fields['password1'].widget.attrs.update({'type': 'password', 'placeholder': 'رمز عبور'})
        self.fields['password2'].widget.attrs.update({'type': 'password', 'placeholder': 'تکرار رمز عبور'})

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ('email', 'username', 'phone', 'first_name', 'last_name', 'is_staff', 'is_superuser',
                  'is_active', 'sex', 'age')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords don\'t match')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password2'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'username', 'phone', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'is_active',
                  'sex', 'age')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
