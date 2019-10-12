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

def job_detail(request):
    card = Card.objects.all()
    context = {
        'job_cards': card
    }
    return render(request, 'job.html', context)

def school_detail(request):
    card = Card.objects.all()
    context = {
        'school_cards': card
    }
    return render(request, 'school.html', context)


# Create your views here.
