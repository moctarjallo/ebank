import unittest

import pythonapi as api

from banking import CreateAccount

class TestCreateAccount(unittest.TestCase):
    def setUp(self):
        self.create_account = CreateAccount()

    def test_normal(self):
        request = api.Request({
            'firstname': 'moctar',
            'lastname': 'diallo',
            'address': 'medina',
            'balance': 400
        })

        account = self.create_account.execute(request.data)
        response = api.Response(account)

        self.assertLess(response.data['code'], 10000)
        self.assertGreaterEqual(response.data['code'], 1)

        del response.data['code']
        self.assertEqual(response.data, {
            'client':{
                'firstname': 'moctar',
                'lastname': 'diallo',
                'address': 'medina',
            },
            'balance': 400,
        })

if __name__ == '__main__':
    unittest.main()