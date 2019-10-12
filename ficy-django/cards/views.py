from django.shortcuts import render
from cards.models import Card

def card_index(request):
    cards = Card.objects.all()
    context = {
        'cards': cards
    }
    return render(request, 'index.html', context)

def children_detail(request):
    card = Card.objects.all()
    context = {
        'children_cards': card
    }
    return render(request, 'children.html', context)


# Create your views here.
