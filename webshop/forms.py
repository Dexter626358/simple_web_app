# myapp/forms.py
from django import forms


class CallBackForm(forms.Form):
    phone_number = forms.CharField(label='Номер телефона', max_length=15)
