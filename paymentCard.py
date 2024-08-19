from abc import ABC, abstractmethod
from cardVerifer import VisaCardVerifer,MasterCardVerifer,AmericanExpressVerifer
from Utility import TransLogger

class PaymentCard(ABC):

    @abstractmethod
    def pay(self,price):
        pass


class VisaCard(PaymentCard):
    
    def __init__(self,cardNumber,ExpirationDate,cvcCode,CardHolder):
        self.__verifer = VisaCardVerifer()
        self.setCardNumber(cardNumber) 
        self.setExpirationDate(ExpirationDate)
        self.setCvcCode(cvcCode)
        self.setCardHolder(CardHolder)


    def setCardNumber(self,cardNumber):
        if(self.__verifer.cardNumberVreifcation(cardNumber)):
            self.__cardNumber = cardNumber
        else:
            raise Exception("[!] Something Went Wrong In The Card Number [!]")
    
    def getCardNumber(self):
        return self.__cardNumber
    
    def setExpirationDate(self,ExpirationDate):
        if(self.__verifer.ExpirationDateVreifcation(ExpirationDate)):
            self.__ExpirationDate = ExpirationDate
        else:
            raise Exception("[!] Something Went Wrong In the Expiration Date [!]")
        
    def getExpirationDate(self):
        return self.__ExpirationDate
    
    def setCardHolder(self,cardHolder):
        self.__cardHolder = cardHolder

    def getCardHolder(self):
        return self.__cardHolder

    def setCvcCode(self,cvcCode):
        if(self.__verifer.cardCodeVreifcation(cvcCode)):
            self.__cvcCode = cvcCode
        else:
            raise Exception("[!] Something Wrong In Your CVC Code [!]")
        
    def getCvcCode(self):
        return self.__cvcCode

    # Visa Card Takes 1% of the Price as a fees
    def pay(self, price):
        return price*1.01
        
class MasterCard(PaymentCard):
    def __init__(self,CardNumber,CardHolder,CardExpirationDate,cvvCode):
        self.__verifer = MasterCardVerifer()
        self.setCardNumber(CardNumber)
        self.setCardHolder(CardHolder)
        self.setCardExpirationDate(CardExpirationDate)
        self.setCvvCode(cvvCode)

    def setCardNumber(self,CardNumber):
        if(self.__verifer.cardNumberVreifcation(CardNumber)):
            self.__cardNumber = CardNumber
        else:
            raise Exception("[!] Something Wrong In Your Card Number [!]")
        
    def getCardNumber(self):
        return self.__cardNumber
    
    def setCardHolder(self,CardHolder):
        self.__cardHolder = CardHolder

    def getCardHolder(self):
        return self.__cardHolder
    
    def setCardExpirationDate(self,CardExpirationDate):
        if(self.__verifer.ExpirationDateVreifcation(CardExpirationDate)):
            self.__cardExpirationDate = CardExpirationDate
        else:
            raise Exception("[!] Something Wrong In Your Card Expiration Date [!]")
        
    def getCardExpirationDate(self):
        return self.__cardExpirationDate
    
    def setCvvCode(self,cvvCode):
        if(self.__verifer.cardCodeVreifcation(cvvCode)):
            self.__cvvCode = cvvCode
        else:
            raise Exception("[!] Someting Wrong In You CVV Code [!]")
        
    def pay(self, price):
        return price*1.15
        


class AmericanExpressCard(PaymentCard):

    def __init__(self,cardNumber,ExpirationDate,cvvCode,cardHolder):
        self.__verifer = AmericanExpressVerifer()
        self.setCardNumber(cardNumber)
        self.setExpirationDate(ExpirationDate)
        self.setCvvCode(cvvCode)
        self.setCardHolder(cardHolder)
        

    def setCardNumber(self,cardNumber):
        if(self.__verifer.cardNumberVreifcation(cardNumber)):
            self.__cardNumber = cardNumber
        else:
            raise Exception("[!] Something Wrong In Your Card Number [!]")
        
    def getCardNumber(self):
        return self.__cardNumber
    
    def setExpirationDate(self,ExpirationDate):
        if(self.__verifer.ExpirationDateVreifcation(ExpirationDate)):
            self.__ExpirationDate = ExpirationDate
        else:
            raise Exception("[!] Something Wrong In Your Expiration Date [!]")
        
    def getExpirationDate(self):
        return self.__ExpirationDate
    
    def setCvvCode(self,cvvCode):
        if(self.__verifer.cardCodeVreifcation(cvvCode)):
            self.__cvvCode = cvvCode
        else:
            raise Exception("[!] Something Wrong In Your CVV Code [!]")
        
    def getCvvCode(self):
        return self.__cvvCode
    
    def setCardHolder(self,cardHolder):
        self.__cardHolder = cardHolder

    def getCardHolder(self):
        return self.__cardHolder
    
    def pay(self, price):
        return price*1.2
    

class BankAccount:

    def __init__(self,balance,paymentCard:PaymentCard):
        self.setBalance(balance)
        self.setPaymentCard(paymentCard)

    def setBalance(self,balance):
        if(balance<0):
            raise Exception("[!] Balance Can't Be Less Than Zero [!]")
        else:
            self.__balance = balance

    def getBalance(self):
        return self.__balance
    
    def setPaymentCard(self,paymentCard:PaymentCard):
        if(PaymentCard not in type(paymentCard).__bases__):
            raise Exception("[!] Insert A Real Payment Card [!]")
        else:
            self.__paymentCard = paymentCard

    def getPaymentCard(self):
        return self.__paymentCard
    
    @TransLogger
    def transfer(self,amount):
        if(amount>0):
            if(self.getPaymentCard().pay(amount)<=self.getBalance()):
                self.setBalance(self.getBalance()-self.getPaymentCard().pay(amount))
                return "Transfer Successful"
            else:
                return "Transfer Failed - No Enough Balance"
        else:
            return "Transfer Denied"