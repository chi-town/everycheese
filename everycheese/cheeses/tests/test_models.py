import pytest 

pytestmark = pytest.mark.django_db

from ..models import Cheese

def test__str__():
    cheese = Cheese.objects.create(
        name="gross",
        description="old squishy cheese",
        firmness=Cheese.Firmness.SOFT,
    )
    assert cheese.__str__() == "gross"
    assert str(cheese) == "gross"