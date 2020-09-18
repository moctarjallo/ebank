import unittest

from ebank.domain.entities import Transaction

class TestTransaction(unittest.TestCase):
    def test_to_dict(self):
        trans = Transaction('deposit', 100, 'moctar', 5221, 300, 400)
        trans_dict = trans.to_dict()
        self.assertEqual(trans_dict, {
            'action': 'deposit',
            'amount': 100,
            'client_name': 'moctar',
            'account_code': 5221,
            'old_balance': 300,
            'new_balance': 400
        })