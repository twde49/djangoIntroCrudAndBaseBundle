from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Message, Response
from .forms import MessageForm, ResponseForm


def all_messages(request):
    messages = Message.objects.all()
    context = {
        "messages": messages
    }

    return render(request, "website/all.html", context)


def show_message(request, id):
    message = Message.objects.get(id=id)
    return render(request, 'website/show.html', {"message": message})


@login_required(login_url="login")
def create_message(request):
    message_form = MessageForm(request.POST or None)
    if message_form.is_valid():
        message = message_form.save(commit=False)
        message.author = request.user
        message.save()
        return redirect("messages")
    return render(request, "website/create.html", {"message_form": message_form})


@login_required(login_url="login")
def update_message(request, id):
    message = get_object_or_404(Message, id=id)
    if message.author != request.user:
        return redirect("messages")
    message_form = MessageForm(request.POST or None, instance=message)
    if message_form.is_valid():
        message = message_form.save(commit=False)
        message.save()
        return redirect("messages")
    return render(request, "website/create.html", {'message_form': message_form})


@login_required(login_url="login")
def message_delete(request, id):
    message = get_object_or_404(Message, id=id)
    if message.author != request.user:
        return redirect("messages")
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
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect("messages")

    return render(request, "website/login.html", {})


def logout_view(request):
    logout(request)
    return redirect("messages")


def add_response(request, id):
    message = get_object_or_404(Message, id=id)
    if message is None:
        redirect("messages")
    response_form = ResponseForm(request.POST or None)
    if response_form.is_valid():
        response = response_form.save(commit=False)
        response.author = request.user
        response.message = message
        response.save()
        return redirect("show_message", message.id)

    return render(request, "website/show.html", {"message": message, 'response_form': response_form})


def response_delete(request, id):
    response = get_object_or_404(Response, id=id)
    if response.author != request.user:
        return redirect("messages")
    if response:
        response.delete()
    return redirect("show_message", response.message.id)


def response_update(request, id):
    response = get_object_or_404(Response, id=id)
    if response.author != request.user:
        return redirect("messages")
    response_form = ResponseForm(request.POST or None, instance=response)
    if response_form.is_valid():
        response = response_form.save(commit=False)
        response.save()
        return redirect("show_message", response.message.id)
    return render(request, "website/updateResponse.html", {"message": response.message, 'response_form': response_form})


