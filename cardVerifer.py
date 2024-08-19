from abc import ABC, abstractmethod
from datetime import datetime

class CardVreifer(ABC):
    @abstractmethod
    def cardNumberVreifcation(self,cardNumber):
        pass

    @abstractmethod
    def ExpirationDateVreifcation(self,ExpirationDate):
        pass

    @abstractmethod
    def cardCodeVreifcation(self,Code):
        pass

class VisaCardVerifer(CardVreifer):

    __instance = None

    def __new__(cls):
        if cls.__instance == None:
            cls.__instance = super(VisaCardVerifer,cls).__new__(cls)
        return cls.__instance

    #The Card Number Vreifcation process include 3 sapreate steps
    #First -> Card number must be 16 digits but it can be up to 19 digits in some cases
    #Second -> Visa Card number must contains only numerical values
    #Third -> Visa Card must start with 4   

    def cardNumberVreifcation(self,cardNumber:int)->bool:
        if(len(cardNumber)>=16 and len(cardNumber)<=19):
            if(cardNumber.isdigit()):
                if(cardNumber.startswith('4')):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
        
    def ExpirationDateVreifcation(self,ExpirationDate:str)->bool:
        month,year = ExpirationDate.split('/')
        cYear = str(datetime.now().year)[-2::]
        cMonth = str(datetime.now().month)

        if(int(cYear)<int(year)):
                return True
        elif(int(cYear) == int(year)):
            if(int(cMonth)<int(month)):
                return True
            else:
                return False
        else:
            return False
        
    def cardCodeVreifcation(self,Code):
        if(len(Code) == 3 or len(Code) == 4):
            if(Code.isdigit()):
                return True
            else:
                False
        else:
            return False
        
class MasterCardVerifer(CardVreifer):
    __instance = None

    def __new__(cls):
        if cls.__instance == None:
            cls.__instance = super(MasterCardVerifer,cls).__new__(cls)
        return cls.__instance

    def cardNumberVreifcation(self,cardNumber):
        if(len(cardNumber) == 16):
            if(cardNumber.isdigit()):
                if(cardNumber.startswith('5') or cardNumber.startswith('2')):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
        
    def ExpirationDateVreifcation(self,ExpirationDate):
        month,year = ExpirationDate.split('/')
        cYear = str(datetime.now().year)[-2::]
        cMonth = str(datetime.now().month)

        if(int(cYear)<int(year)):
            return True
        
        elif(int(cYear) == int(year)):
            if(int(cMonth)<int(month)):
                return True
            else:
                return False
    
        else:
            return False
        
    def cardCodeVreifcation(self,Code):
        if(len(Code) == 3):
            if(Code.isdigit()):
                return True
            else:
                return False
        else:
            return False

class AmericanExpressVerifer(CardVreifer):
    __instance = None

    def __new__(cls):
        if cls.__instance == None:
            cls.__instance = super(AmericanExpressVerifer,cls).__new__(cls)
        return cls.__instance
    
    def cardNumberVreifcation(self,cardNumber):
        if(len(cardNumber) == 15):
            if(cardNumber.isdigit()):
                if(cardNumber.startswith('37') or cardNumber.startswith('34')):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
        
    def ExpirationDateVreifcation(self,ExpirationDate):
        month,year = ExpirationDate.split('/')
        cYear = str(datetime.now().year)[-2::]
        cMonth = str(datetime.now().month)

        if(int(cYear)<int(year)):
            return True
        elif(int(cYear) == int(year)):
            if(int(cMonth)<int(month)):
                return True
            else:
                return False
        else:
            return False
        
    def cardCodeVreifcation(self,Code):
        if(len(Code) == 3):
            if(Code.isdigit()):
                return True
            else:
                return False
        else:
            return False
