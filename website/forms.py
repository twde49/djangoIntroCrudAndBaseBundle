from django.contrib.auth.models import User
from django.forms import Textarea, ModelForm
from website.models import Message, Category, Response
from django import forms


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ["title", "content", "category"]
        widgets = {
            "content": Textarea(attrs={"rows": 5})
        }

    category = forms.ModelChoiceField(queryset=Category.objects.all())


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]


class ResponseForm(ModelForm):
    class Meta:
        model = Response
        fields = ["content"]
