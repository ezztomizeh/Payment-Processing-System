from Logging import TransactionLogger

logger = TransactionLogger('localhost',6379)
logger.setServerAddress('localhost')
logger.setServerPort(6379)
logger.connect()

TransLogger = logger.logger