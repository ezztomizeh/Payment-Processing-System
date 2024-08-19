from datetime import datetime
from abc import ABC,abstractmethod
import redis

class Logger(ABC):

    @abstractmethod
    def logger(self,func):
        pass


class TransactionLogger(Logger):

    __instance = None
    __connection = None

    def __new__(cls,*args,**kwargs):
        if cls.__instance == None:
            cls.__instance = super(TransactionLogger,cls).__new__(cls)
        return cls.__instance
    
    def __init__(self,serverAddress,serverPort):
        self.setServerAddress(serverAddress)
        self.setServerPort(serverPort)

    def setServerAddress(self,serverAddress):
        self.__serverAddress = serverAddress
    
    def getServerAdress(self):
        return self.__serverAddress
    
    def setServerPort(self,serverPort):
        self.__serverPort = serverPort

    def getServerPort(self):
        return self.__serverPort
    
    def connect(self):
        if self.__connection == None:
            self.__connection = redis.Redis(self.getServerAdress(),self.getServerPort())
    
    def logger(self,func):
        def wrapper(*args,**kwargs):
            if self.__connection:
                status = func(*args,**kwargs)
                self.__connection.set(str(datetime.now()),f'{status}: Transfer {args[-1]} Using {type(args[0].getPaymentCard())}')
                return status
            else:
                raise Exception("[!] Failed To Write On The Sever [!]")
        return wrapper
    
    def disconnect(self):
        if self.__connection:
            self.__connection.close()
            self.__connection = None