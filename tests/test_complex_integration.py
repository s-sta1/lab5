from src.manager import Manager
from src.models import Parameters

def test_correct_payment_month():
    manager = Manager(Parameters())
    
    total = manager.get_apartment_costs("apart-polanka", 2025, 1)
    assert total == 910.00
    
def test_empty_payment_month():
    manager = Manager(Parameters())
    
    total = manager.get_apartment_costs("apart-polanka", 2026, 1)
    assert total == 0.0
    
def test_wrong_apart_name():
    manager = Manager(Parameters())
    
    total = manager.get_apartment_costs("apart-piatkowo", 2025, 1)
    assert total is None