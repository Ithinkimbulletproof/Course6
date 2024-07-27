from django.shortcuts import render, get_object_or_404, redirect
from .models import Client, Message, Mailing
from .forms import ClientForm, MessageForm, MailingForm


# Утилита для обработки форм
def handle_form(request, form_class, instance=None, redirect_url="client_list"):
    if request.method == "POST":
        form = form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(redirect_url)
    else:
        form = form_class(instance=instance)
    return form


def client_list(request):
    clients = Client.objects.all()
    return render(request, "main/client_list.html", {"clients": clients})


def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    return render(request, "main/client_detail.html", {"client": client})


def client_create(request):
    form = handle_form(request, ClientForm)
    return render(request, "main/client_form.html", {"form": form})


def client_update(request, pk):
    client = get_object_or_404(Client, pk=pk)
    form = handle_form(request, ClientForm, instance=client)
    return render(request, "main/client_form.html", {"form": form})


def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
        client.delete()
        return redirect("client_list")
    return render(request, "main/client_confirm_delete.html", {"client": client})


def message_list(request):
    messages = Message.objects.all()
    return render(request, "main/message_list.html", {"messages": messages})


def message_detail(request, pk):
    message = get_object_or_404(Message, pk=pk)
    return render(request, "main/message_detail.html", {"message": message})


def message_create(request):
    form = handle_form(request, MessageForm)
    return render(request, "main/message_form.html", {"form": form})


def message_update(request, pk):
    message = get_object_or_404(Message, pk=pk)
    form = handle_form(request, MessageForm, instance=message)
    return render(request, "main/message_form.html", {"form": form})


def message_delete(request, pk):
    message = get_object_or_404(Message, pk=pk)
    if request.method == "POST":
        message.delete()
        return redirect("message_list")
    return render(request, "main/message_confirm_delete.html", {"message": message})


def mailing_list(request):
    mailings = Mailing.objects.all()
    return render(request, "main/mailing_list.html", {"mailings": mailings})


def mailing_detail(request, pk):
    mailing = get_object_or_404(Mailing, pk=pk)
    return render(request, "main/mailing_detail.html", {"mailing": mailing})


def mailing_create(request):
    form = handle_form(request, MailingForm)
    return render(request, "main/mailing_form.html", {"form": form})


def mailing_update(request, pk):
    mailing = get_object_or_404(Mailing, pk=pk)
    form = handle_form(request, MailingForm, instance=mailing)
    return render(request, "main/mailing_form.html", {"form": form})


def mailing_delete(request, pk):
    mailing = get_object_or_404(Mailing, pk=pk)
    if request.method == "POST":
        mailing.delete()
        return redirect("mailing_list")
    return render(request, "main/mailing_confirm_delete.html", {"mailing": mailing})


def home(request):
    return render(request, "main/home.html")
