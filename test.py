# test slightly bigger equation

"""
def circle_area(radius):
    return 3.142 * radius**2


def test_area():
    assert circle_area(4) == 50.272
"""


class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def add_to_balance(self, amount):
        self.balance += amount
        return self.balance


account = Account()


def test_balance():
    assert account.add_to_balance(20000) == 20000
