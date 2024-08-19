from paymentCard import VisaCard,MasterCard,AmericanExpressCard,BankAccount
from Products import Product,Order

# Availabe Products

banana = Product('banana',50)
apple = Product('apple',20)
cola = Product('cola',30)

# Customers

visa = VisaCard('4606402617845688','10/28','277','ezz')
master = MasterCard('5481094173442336','ezzudin','01/25','000')
american = AmericanExpressCard('379435696086090','11/28','199','ezzudin')

acc1 = BankAccount(1000,visa)
acc2 = BankAccount(1000,master)
acc3 = BankAccount(1000,american)

# Orders

order1 = Order()
order1.addItems(banana,apple)

order2 = Order()
order2.addItems(cola)

order3 = Order()
order3.addItems(banana,cola)

# Payment
acc1.transfer(order1.CalculateAmount())
acc2.transfer(order2.CalculateAmount())
acc3.transfer(order3.CalculateAmount())