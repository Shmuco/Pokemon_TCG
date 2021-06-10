from card_game.models import Transaction
from django.shortcuts import get_object_or_404, render,redirect
from .forms import *
from django.views import generic
from django.urls import reverse_lazy
from django.conf import settings



# Create your views here.

def homepage(request):

    return render(request, 'homepage.html')

def open_sales(request):
    sales = OpenSale.objects.filter(status = True).exclude(seller = request.user)

    return render(request, 'open_sales.html', {'sales': sales})


def new_sale (request):
    if request.method == 'POST':
        form = SaleForm(request.user, request.POST)
        if form.is_valid:
            f = form.save(commit=False)
            f.seller = request.user
            f.save()
            return redirect('open_sales')
    else:
        form = SaleForm (request.user)
    return render(request, 'selling_form.html', {'form': form})

def new_offer (request, s_id):
    if request.method == 'POST':
        form = OfferForm(request.user, request.POST)
        if form.is_valid:
            f = form.save(commit=False)
            f.buyer = request.user
            f.sale = OpenSale.objects.get(id = s_id)
            f.save()
            return redirect('open_sales')
    else:
        form = SaleForm (request.user)
    return render(request, 'selling_form.html', {'form': form})

def my_open_sales(request):
    sales = OpenSale.objects.filter(seller = request.user, status = True)
    return render(request, 'my_open_sales.html', {'sales': sales})

def view_offers(request, s_id):
    offers = PendingOffers.objects.filter(sale = s_id, status = True)
    print(s_id)
    print(offers)
    return render(request, 'view_offers.html', {'offers': offers})

def my_deck(request):
    deck = Deck.objects.get(user = request.user)
    print(deck)
    # print(deck.cards)
    cards = deck.cards.all()
    print(cards)
    return render(request, 'test_page.html', {'cards': cards})

def offer_accepted(request, o_id):
    offer = PendingOffers.objects.get(id= o_id)
    incoming_card = offer.card
    outgoing_card = offer.sale.card
    seller = offer.sale.seller
    buyer = offer.buyer
    Transaction.objects.create(seller = seller,buyer = buyer, card_sold = outgoing_card, exchanged_for = incoming_card)
    buyer.deck.cards.remove(incoming_card)
    buyer.deck.cards.add(outgoing_card)
    seller.deck.cards.remove(outgoing_card)
    seller.deck.cards.add(incoming_card)
    print(offer.status)
    offer.status = False
    offer.save()
    print(offer.status)
    offer.sale.status = False
    offer.sale.save()

    return redirect('my_deck')

def offer_rejected(request, o_id):
    offer = PendingOffers.objects.get(id= o_id)
    print(offer.status)
    offer.status = False
    offer.save()
    
    return redirect('my_deck')


def my_offers(request):
    offers = PendingOffers.objects.filter(buyer = request.user, status = True)

    return render (request, 'my_offers.html', {'offers': offers})
    
def delete_sale(request, s_id):
    sale = OpenSale.objects.get(id = s_id)
    print(sale)
    sale.status = False
    sale.save()
    return redirect ('my_open_sales')
    







# def buying (request, t_id):
#     if request.method == 'POST':
#         transaction = get_object_or_404(Transaction, id=t_id)
#         print(transaction.seller.id)
#         form = BuyingForm(request.user, request.POST, instance=transaction)
#         if form.is_valid:
#             transaction = form.save()
#             transaction.buyer = request.user
#             transaction.save()
#             return redirect('all_transactions')
#     else:
#         form = BuyingForm(request.user)
#     return render(request, 'selling_form.html', {'form': form})