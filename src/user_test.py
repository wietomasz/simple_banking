import unittest
from accounts import User

class TestUser(unittest.TestCase):

    def test_deposit_for_account(self):
        account = User(1, 0, 0, 0, False)
        account.deposit(4)
        self.assertEqual(4, account.available)
        self.assertEqual(4, account.total)

    def test_withdrawal_for_account(self):
        account = User(1, 3, 0, 3, False)
        account.withdraw(2)
        self.assertEqual(1, account.available)
        self.assertEqual(1, account.total)

    def test_dispute_for_account(self):
        account = User(1, 0, 0, 0, False)
        account.deposit(4)
        account.dispute(1)
        self.assertEqual(3, account.available)
        self.assertEqual(1, account.held)

    def test_resolve_for_account(self):
        account = User(1, 0, 0, 0, False)
        account.deposit(4)
        account.dispute(1)
        account.resolve(1)
        self.assertEqual(4, account.available)
        self.assertEqual(0, account.held)

    def test_chargeback_for_account(self):
        account = User(1, 0, 0, 0, False)
        account.deposit(4)
        account.dispute(1)
        account.chargeback(1)
        self.assertEqual(3, account.total)
        self.assertEqual(3, account.available)
        self.assertEqual(True, account.locked)

    def test_withdrawal_for_account_negative(self):
        account = User(1, 3, 0, 3, False)
        account.withdraw(4)
        self.assertEqual(3, account.available)
        self.assertEqual(3, account.total)