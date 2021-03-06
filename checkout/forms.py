from django import forms
from .models import Order


class MakePaymentForm(forms.Form):

    MONTH_CHOICES = [(i, i) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i) for i in range(2020, 2072)]

    credit_card_number = forms.CharField(label='Credit Card Number', required=True)
    cvv = forms.CharField(label='CVV Number', required=True)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=True)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=True)
    stripe_id = forms.CharField(widget=forms.HiddenInput)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('user', 'first_name', 'last_name', 'address1', 'address2', 'city', 'postcode')
        widgets = {'user': forms.HiddenInput()}
