import pytest 
from .factories import CheeseFactory

pytestmark = pytest.mark.django_db

from ..models import Cheese

def test__str__():
    cheese = CheeseFactory(name="Stracchino")
    assert cheese.__str__() == "Stracchino"
    assert str(cheese) == "Stracchino"

def test_get_absolute_url():
    cheese = CheeseFactory()
    url = cheese.get_absolute_url()
    assert url == f'/cheeses/{cheese.slug}/'