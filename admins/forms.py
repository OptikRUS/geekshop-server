from django import forms
from django.forms import ModelForm

from users.forms import UserRegistrationForm, UserProfileForm
from users.models import User
from products.models import ProductCategory


class UserAdminRegistrationForm(UserRegistrationForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'username', 'email',
                  'password1', 'password2',
                  'telegram_username', 'age'
                  )


class UserAdminProfileForm(UserProfileForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control py-4'}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control py-4', 'placeholder': 'Возраст'}),
                             required=False)


class CategoryAdminRegistrationForm(ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Название категории'}))
    description = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Описание'}))

    class Meta:
        model = ProductCategory
        fields = ('name', 'description')


class CategoryAdminEditForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))

    class Meta:
        model = ProductCategory
        fields = ('name', 'description')
