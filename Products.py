from paymentCard import PaymentCard

class Product:
    def __init__(self,productName,productPrice):
        self.setProductName(productName)
        self.setProductPrice(productPrice)
    
    def setProductName(self,productName):
        self.__productName = productName

    def getProductName(self):
        return self.__productName
    
    def setProductPrice(self,price):
        if(price>0):
            self.__productPrice = price
        else:
            raise Exception("[!] Product Price Can't Be Less Than Zero [!]")
        
    def getProductPrice(self):
        return self.__productPrice
    
class Order:
    def __init__(self):
        self.__cart = []

    def addItems(self,*product:Product):
        for pro in product:
            self.__cart.append(pro)
    
    def getItems(self):
        return self.__cart
    
    def CalculateAmount(self):
        amount = 0
        for product in self.getItems():
            amount += product.getProductPrice()
        return amount