class Products:
    def __init__(self, title, unitPrice, discount) -> None:
        self.title = title
        self.unitPrice = unitPrice
        self.temp = [unitPrice, discount]
        self.strikePrice = self.temp
        self.discount = discount

    @property
    def strikePrice(self):
        return self.unitPrice*self.discount/100

    @strikePrice.setter
    def strikePrice(self, ls):
        print(ls)
        self.strikePrice = ls[0]*ls[1]/100


Book = Products('Maths', 120, 10)
# Book.strikePrice = 100
# print(Book.strikePrice)
