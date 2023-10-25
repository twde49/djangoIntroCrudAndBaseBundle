from django.shortcuts import render, redirect, get_object_or_404
from .models import Message
from .forms import MessageForm



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
        message_form.save()
        return redirect("messages")
    return render(request, "website/create.html", {'message_form': message_form})


def message_delete(request, id):
    message = get_object_or_404(Message, id=id)
    if message:
        message.delete()
    return redirect("messages")
