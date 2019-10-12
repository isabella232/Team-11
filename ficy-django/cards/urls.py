from django.urls import path
from . import views

urlpatterns = [
    path("", views.card_index, name="index"),
    path("children", views.children_detail, name="children"),
]
