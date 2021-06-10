from django import forms
from .models import *

class SaleForm(forms.ModelForm):
    class Meta:
        model = OpenSale
        fields = ('card',)

    def __init__(self, user, *args, **kwargs):
        super(SaleForm, self).__init__(*args, **kwargs)
        cards = Card.objects.filter(deck=Deck.objects.get(user=user))
        self.fields['card'].queryset = cards


class OfferForm(forms.ModelForm):
    class Meta:
        model = PendingOffers
        fields = ('card',)

    def __init__(self, user, *args, **kwargs):
        super(OfferForm, self).__init__(*args, **kwargs)
        cards = Card.objects.filter(deck=Deck.objects.get(user=user))
        self.fields['card'].queryset = cards

