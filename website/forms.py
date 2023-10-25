from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea
from website.models import Message


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ["title", "content"]
        widgets = {
            "content": Textarea(attrs={"rows": 5})
        }


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]
