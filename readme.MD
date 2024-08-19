# Payment Processing System

## Overview

This project is a simplified payment processing system that simulates the validation and transaction process for different types of payment cards (Visa, MasterCard, and American Express). The system also manages products, orders, and bank accounts to facilitate payments.

## Project Structure

- **cardVerifier.py**: Contains the card verification logic for Visa, MasterCard, and American Express cards. Each card type has its own verification rules for the card number, expiration date, and CVC/CVV code.
  
- **logging.py**: Implements a logging system using Redis to store transaction logs. The `TransactionLogger` class is a singleton that manages connection to a Redis server and logs transaction details.

- **Utility.py**: Contains utility functions and sets up the logger for transaction logging.

- **paymentCard.py**: Defines different payment card types (`VisaCard`, `MasterCard`, and `AmericanExpressCard`) and a `BankAccount` class that interacts with these cards to perform transactions.

- **Products.py**: Manages products and orders. The `Product` class represents an individual product, and the `Order` class handles multiple products and calculates the total amount for an order.

- **test.py**: A test script that demonstrates the functionality of the system. It creates products, customers with different cards, and executes transactions.

## Getting Started

### Prerequisites

- Python 3.x
- Redis server (running locally on `localhost` at port `6379`)

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install required Python packages:
   ```bash
   pip install redis
   ```

3. Start the Redis server:
   ```bash
   redis-server
   ```

### Running the Test Script

To test the payment processing system, run the `test.py` script:

```bash
python test.py
```

The script will:
- Create several products.
- Create customers with different payment cards (Visa, MasterCard, American Express).
- Create orders and attempt to pay using the associated bank accounts.
- Log the transaction details in the Redis server.

### Redis Logs

Transaction logs are stored in the Redis server with timestamps as keys. Each log entry records the status of the transaction and the details of the payment card used.

## Class Descriptions

### `CardVerifier.py`

- **CardVreifer (Abstract Base Class)**: Abstract base class for card verification.
- **VisaCardVerifer**: Singleton class that verifies Visa card details.
- **MasterCardVerifer**: Singleton class that verifies MasterCard details.
- **AmericanExpressVerifer**: Singleton class that verifies American Express card details.

### `Logging.py`

- **Logger (Abstract Base Class)**: Abstract base class for logging.
- **TransactionLogger**: Singleton class for logging transactions to a Redis server.

### `Utility.py`

- **TransLogger**: A decorator function for logging transaction details using the `TransactionLogger`.

### `PaymentCard.py`

- **PaymentCard (Abstract Base Class)**: Abstract base class for payment cards.
- **VisaCard**: Represents a Visa card and handles payments.
- **MasterCard**: Represents a MasterCard and handles payments.
- **AmericanExpressCard**: Represents an American Express card and handles payments.
- **BankAccount**: Manages a bank account associated with a payment card and handles transactions.

### `Products.py`

- **Product**: Represents a product with a name and price.
- **Order**: Manages a list of products and calculates the total amount.

## Notes

- The payment system simulates real-world scenarios by applying different fees for each card type:
  - Visa: 1% of the transaction amount.
  - MasterCard: 15% of the transaction amount.
  - American Express: 20% of the transaction amount.
- The system includes basic error handling for invalid card details, insufficient funds, and other common issues.

## Future Improvements

- Add more card types and verification rules.
- Implement a user interface for easier interaction.
- Enhance the logging system with more detailed transaction information.
- Integrate with an actual payment gateway for real transactions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
