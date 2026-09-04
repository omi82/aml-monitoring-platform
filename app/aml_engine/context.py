from collections import defaultdict


class AMLContext:
    """
    Shared context for all AML rules.

    Pre-computes commonly used transaction groupings
    to avoid repeated processing inside individual rules.
    """

    def __init__(self, transactions):

        self.transactions = transactions

        # Groupings
        self.by_customer = defaultdict(list)
        self.by_account = defaultdict(list)
        self.deposits_by_customer = defaultdict(list)
        self.withdrawals_by_customer = defaultdict(list)

        for txn in transactions:

            self.by_customer[txn.customer_id].append(txn)

            self.by_account[txn.account_number].append(txn)

            txn_type = txn.transaction_type.lower()

            if txn_type == "deposit":
                self.deposits_by_customer[
                    txn.customer_id
                ].append(txn)

            elif txn_type == "withdrawal":
                self.withdrawals_by_customer[
                    txn.customer_id
                ].append(txn)

        # Sort all transaction lists chronologically

        for txns in self.by_customer.values():
            txns.sort(key=lambda t: t.transaction_timestamp)

        for txns in self.by_account.values():
            txns.sort(key=lambda t: t.transaction_timestamp)

        for txns in self.deposits_by_customer.values():
            txns.sort(key=lambda t: t.transaction_timestamp)

        for txns in self.withdrawals_by_customer.values():
            txns.sort(key=lambda t: t.transaction_timestamp)