class Product:
    def __init__(self, name, price, quantity) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity

    def toDBCollection(self):
        return {
            'name': self.name,
            'price': self.price,
            'quantity':self.quantity
        }