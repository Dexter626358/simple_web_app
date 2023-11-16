import random
from datetime import date
from decimal import Decimal
from django.shortcuts import render
from webshop.forms import CallBackForm
from webshop.models import Product
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm, LoginForm


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
            'price': round(Decimal(random.uniform(1.0, 1000.0)), 2),
            'description': f"{random.choice(adjectives)} {random.choice(nouns)}",
            'quantity': random.randint(1, 100),
            'added_date': date.today(),
            'image': f'path/to/image{i}.jpg',
        }
        products.append(product)
    # products = Product.objects.all()
    return render(request, 'webshop/product_list.html', {'products': products})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'webshop/success_registration.html')  # Замените 'home' на URL вашей домашней страницы
    else:
        form = RegistrationForm()
    return render(request, 'webshop/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('webshop/success_registration.html')  # Замените 'home' на URL вашей домашней страницы
    else:
        form = LoginForm()
    return render(request, 'webshop/login.html', {'form': form})
