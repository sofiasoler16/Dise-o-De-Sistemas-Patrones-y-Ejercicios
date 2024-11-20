from delivery import Delivery
from payment_getawey import PaymentGetaway
from inventory import Inventory

class OnlineShoppingFacade:
    def __init__(self):
        self.inventory = Inventory()
        self.payment = PaymentGetaway()
        self.delivery = Delivery()

    def buy_item(self, item, amount):
        if self.inventory.check_stock(item):
            self.payment.process_payment(amount)
            self.delivery.delivery(item)