from app.data_generator.customer_generator import CustomerGenerator
from app.data_generator.account_generator import AccountGenerator
from app.data_generator.transaction_generator import TransactionGenerator

def main():

    customer_generator = CustomerGenerator()
    customer_generator.generate()
    customer_generator.save()

    account_generator = AccountGenerator(
        customer_generator.customers
    )

    account_generator.generate()
    account_generator.save()

    transaction_generator = TransactionGenerator(
        customer_generator.customers,
        account_generator.accounts,
    )

    transaction_generator.generate()
    transaction_generator.save()

if __name__ == "__main__":
    main()