from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

import random



# Create your models here.

class Card(models.Model):
    name = models.CharField(max_length=200)
    pokemon_id = models.IntegerField()
    capture_rate = models.IntegerField()
    is_legendary = models.BooleanField()
    description = models.TextField(max_length=1000)
    ptype = models.ManyToManyField('PokemonType')
    image = models.URLField(default = 'https://bit.ly/3g48hBf')

    def __str__(self):
        return self.name

   
class Deck(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cards = models.ManyToManyField(Card)

class PokemonType(models.Model):
    ptype= models.CharField(max_length=200)


@receiver(post_save, sender=User)
def create_deck(sender, created, instance, **kwargs):
    cards = Card.objects.all()
    if created:
        deck = Deck.objects.create(user=instance)
        print(deck)
        for i in range(20):
            print(i)
            new_card = random.choice(cards)
            print(new_card)
            deck.cards.add(new_card.id)
        
        


class Transaction(models.Model):
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'seller', on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, blank =True, null=True, related_name = 'buyer', on_delete=models.CASCADE)
    card_sold = models.ForeignKey(Card, blank =True, null=True,related_name = 'card_for_sale' , on_delete=models.CASCADE)
    exchanged_for = models.ForeignKey(Card, blank =True, null=True,on_delete=models.CASCADE)
    compleated = models.DateTimeField(auto_now_add=True)


class OpenSale(models.Model):
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    sale_opened = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

class PendingOffers(models.Model):
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    sale = models.ForeignKey(OpenSale, on_delete=models.CASCADE)
    offer_opened = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    

