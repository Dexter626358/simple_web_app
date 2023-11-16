import random
from datetime import date
from decimal import Decimal

from django.shortcuts import render

from webshop.forms import CallBackForm
from webshop.models import Product


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


def order_call(request):
    if request.method == 'POST':
        form = CallBackForm(request.POST)
        if form.is_valid():
            # Ваш код обработки заказа звонка
            # Здесь вы можете добавить логику для отправки уведомления или сохранения заказа в базу данных

            return render(request, 'webshop/thank_you.html')
    else:
        form = CallBackForm()

    return render(request, 'webshop/order_call.html', {'form': form})


def product_list(request):
    adjectives = ['Прекрасный', 'Строгий', 'Элегантный', 'Современный', 'Удобный']
    nouns = ['стул', 'стол', 'диван', 'кресло', 'шкаф']
    products = []
    for i in range(1, 11):
        product = {
                'name': f'Product {i}',
                'price': Decimal(random.uniform(1.0, 1000.0)),
                'description': f"{random.choice(adjectives)} {random.choice(nouns)}",
                'quantity': random.randint(1, 100),
                'added_date': date.today(),
                'image': f'path/to/image{i}.jpg',
            }
        products.append(product)
    #products = Product.objects.all()
    return render(request, 'webshop/product_list.html', {'products': products})