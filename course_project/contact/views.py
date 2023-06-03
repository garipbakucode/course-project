from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def contact(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Müraciətiniz uğurla qeydə alındı, tezliklə sizinlə əlaqə saxlanılacaq')
            return redirect(reverse_lazy("contact"))
    context = {
        'form': form,
    }
    return render(request, "contact/index.html", context)
