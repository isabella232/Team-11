from django.shortcuts import render
from cards.models import Card

def card_index(request):
    cards = Card.objects.all()
    context = {
        'cards': cards
    }
    return render(request, 'index_html', context)

def card_detail(request):
    card = Card.objects
    context = {
        'card': card
    }
    return render(request, 'children.html', context)


# Create your views here.
