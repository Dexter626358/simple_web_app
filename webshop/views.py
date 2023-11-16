from django.shortcuts import render


# Create your views here.

def welcome_view(request):
    content = {
        "greetings": "Добро пожаловать в наш интренет-магазин!"
    }
    return render(request, 'webshop/base.html', context=content)


def contacts(request):
    contact = {
        'name': 'Виртуальный магазинчик',
        'Email': 'hello@virtualmart.com',
        'address': 'Ул. Виртуальная, д. 456, Город, Страна',
        'phone': '+79456878374',
    }
    return render(request, 'webshop/contacts.html', context=contact)
