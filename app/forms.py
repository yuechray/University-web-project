from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Task, Comment, Review

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ""
        self.fields['username'].label = ""
        self.fields['username'].widget = forms.TextInput(attrs={
            "autocomplete": "off",
            "placeholder": "Имя пользователя",
            'class': 'form-control input-find'
        })

        self.fields['email'].help_text = ""
        self.fields['email'].label = ""
        self.fields['email'].widget = forms.TextInput(attrs={
            "autocomplete": "off",
            "type": "email",
            "placeholder": "Email",
            'class': 'form-control input-find'
        })

        self.fields['password1'].label = ""
        self.fields['password1'].widget = forms.PasswordInput(attrs={
            "autocomplete": 'new-password',
            "placeholder": "Пароль",
            'class': 'form-control input-find'
        })

        self.fields['password2'].label = ""
        self.fields['password2'].widget = forms.PasswordInput(attrs={
            "autocomplete": 'new-password',
            "placeholder": "Подтвердите пароль",
            'class': 'form-control input-find'
        })


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ""
        self.fields['username'].label = ""
        self.fields['password'].label = ""
        self.fields['password'].widget = forms.TextInput(attrs={
            "type": "password",
            "placeholder": "Пароль",
            'class': 'form-control'
        })
        self.fields['username'].widget = forms.TextInput(attrs={
            "placeholder": "Имя пользователя",
            'class': 'form-control'
        })


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task", "image", ]

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['title'].help_text = ""
        self.fields['title'].label = ""
        self.fields['title'].widget = forms.Textarea(attrs={
            "placeholder": "Название новости",
            "rows": 1,
            'class': 'form-control'})

        self.fields['task'].help_text = ""
        self.fields['task'].label = ""
        self.fields['task'].widget = forms.Textarea(attrs={
            "placeholder": "Содержание новости",
            "rows": 10,
            'class': 'form-control'})


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['text'].help_text = ""
        self.fields['text'].label = ""
        self.fields['text'].widget = forms.Textarea(attrs={
            "placeholder": "Текст комментария",
            "rows": 1,
            'class': 'form-control'})


class UserUpdate(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password", "last_name", "first_name", "email"]


from django import forms
from .models import Review, Product

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["text", "image"]
        widgets = {
            'text': forms.Textarea(attrs={
                "placeholder": "Оставьте свой отзыв...",
                "rows": 4,
                "class": "form-control"
            }),
            'image': forms.ClearableFileInput(attrs={
                "class": "form-control"
            })
        }
        labels = {
            'text': 'Содержание',
            'image': 'Изображение'
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "manufacturer", "image"]
        widgets = {
            'name': forms.TextInput(attrs={
                "placeholder": "Название товара",
                "class": "form-control"
            }),
            'description': forms.Textarea(attrs={
                "placeholder": "Описание товара",
                "rows": 5,
                "class": "form-control"
            }),
            'price': forms.NumberInput(attrs={
                "placeholder": "Цена",
                "class": "form-control",
                "step": "0.01"
            }),
            'manufacturer': forms.TextInput(attrs={
                "placeholder": "Производитель",
                "class": "form-control"
            }),
            'image': forms.ClearableFileInput(attrs={
                "class": "form-control"
            })
        }
        labels = {
            'name': 'Название',
            'description': 'Описание',
            'price': 'Цена',
            'manufacturer': 'Производитель',
            'image': 'Изображение'
        }
        