from django.conf import settings
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Message
from .forms import MessageForm
from django.contrib.auth.models import User


def all_messages(request):
    messages = Message.objects.all()
    context = {
        "messages": messages
    }

    return render(request, "website/all.html", context)


def show_message(request, id):
    message = Message.objects.get(id=id)
    return render(request, 'website/show.html', {"message": message})


def create_message(request):
    message_form = MessageForm(request.POST or None)
    if message_form.is_valid():
        message_form.save()
        return redirect("messages")
    return render(request, "website/create.html", {"message_form": message_form})


def update_message(request, id):
    message = get_object_or_404(Message, id=id)
    message_form = MessageForm(request.POST or None, instance=message)
    if message_form.is_valid():
        message = message_form.save(commit=False)
        message.save()
        return redirect("messages")
    return render(request, "website/create.html", {'message_form': message_form})


def message_delete(request, id):
    message = get_object_or_404(Message, id=id)
    if message:
        message.delete()
    return redirect("messages")


def register_view(request):
    user_form = UserCreationForm(request.POST or None)
    if user_form.is_valid():
        user = user_form.save()
        user.save()
        return redirect("messages")
    return render(request, "website/register.html", {"user_form": user_form})


def login_view(request):
    user_form = (request.POST or None)
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        login(request, user)
        return redirect("messages")

    return render(request, "website/login.html", {"user_form": user_form})


def logout_view(request):
    logout(request)
    return redirect("messages")
