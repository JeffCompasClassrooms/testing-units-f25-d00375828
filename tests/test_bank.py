from bank import *

class TestBank:

    def test_default_balance(self):
        account = BankAccount("Andy")
        assert account.get_balance() == 0.0

    def test_owner_stored(self):
        account = BankAccount("Andie Sonju", 100000)
        assert account.owner == "Andie Sonju"

    def test_lowercase_owner(self):
        account = BankAccount("paul")
        assert account.get_balance() == 0.0

    def test_uppercase_owner(self):
        account = BankAccount("JEFF")
        assert account.get_balance() == 0.0
    
    def test_float_balance(self):
        account = BankAccount("Andy", 50)
        assert isinstance(account.get_balance(), float)

    def test_neg_balance(self):
        try:
            BankAccount("Mike", -25)
            assert False, "Expected ValueError"
        except ValueError as e:
            assert "Balance cannot be negative" in str(e)

    def test_deposit_returns_balance(self):
        account = BankAccount("Ben", 10)
        new_bal = account.deposit(5)
        assert new_bal == 15.0
        assert account.get_balance() == 15.0

    def test_deposit_increases_balance(self):
        account = BankAccount("Dana", 50)
        account.deposit(20)
        assert account.get_balance() == 70.0
        assert account.last_transaction() == ("deposit", 20)

    def test_deposit_zero(self):
        account = BankAccount("Zak", 10.0)
        try:
            account.deposit(0)
            assert False, "Expected ValueError"
        except ValueError as e:
            assert "Deposit must be positive" in str(e)
        assert account.get_balance() == 10.0

    def test_deposit_neg(self):
        account = BankAccount("Leslye", 30.0)
        try:
            account.deposit(-5)
            assert False
        except ValueError as e:
            assert account.get_balance() == 30.0

    def test_withdraw_returns_new_balance(self):
        account = BankAccount("Cara", 20)
        new_bal = account.withdraw(7.5)
        assert new_bal == 12.5
        assert account.get_balance() == 12.5

    def test_withdraw_(self):
        account = BankAccount("Frank", 100)
        account.withdraw(40)
        assert account.get_balance() == 60.0
        assert account.last_transaction() == ("withdraw", 40)
    
    def test_withdraw_zero(self):
        account = BankAccount("Todd", 10.0)
        try:
            account.withdraw(0)
            assert False
        except ValueError as e:
            assert account.get_balance() == 10.0 

    def test_withdraw_neg(self):
        account = BankAccount("Will", 10.0)
        try:
            account.withdraw(-1)
            assert False
        except ValueError as e:
            assert account.get_balance() == 10.0 

    def test_withdraw_all(self):
        account = BankAccount("Tony", 20.0)
        account.withdraw(20.0)
        assert account.get_balance() == 0.0
        assert account.last_transaction() == ("withdraw", 20.0)

    def test_withdraw_more_than_balance(self):
        account = BankAccount("Grace", 30)
        try:
            account.withdraw(50)
            assert False, "Expected ValueError"
        except ValueError as e:
             assert "Insufficient funds" in str(e)

    def test_transfer_money_between_accounts(self):
        account1 = BankAccount("Heidi", 100)
        account2 = BankAccount("Ivan", 50)
        account1.transfer_to(account2, 40)
        assert account1.get_balance() == 60
        assert account2.get_balance() == 90

    def test_transfer_money_float(self):
        account1 = BankAccount("Rob", 900)
        account2 = BankAccount("Bob", 550)
        account1.transfer_to(account2, 300.25)
        assert account1.get_balance() == 599.75
        assert account2.get_balance() == 850.25

    def test_transfer_basic_success(self):
        a = BankAccount("A", 100.0)
        b = BankAccount("B", 25.0)
        src_bal, dst_bal = a.transfer_to(b, 40.0)
        assert src_bal == 60.0
        assert dst_bal == 65.0
        assert a.get_balance() == 60.0
        assert b.get_balance() == 65.0

    def test_transfer_to_zero(self):
        a = BankAccount("A", 75.0)
        b = BankAccount("B", 10.0)
        a.transfer_to(b, 75.0)
        assert a.get_balance() == 0.0
        assert b.get_balance() == 85.0

    def test_transfer_insufficient_funds(self):
        a = BankAccount("A", 30.0)
        b = BankAccount("B", 5.0)
        try:
            a.transfer_to(b, 50.0)
            assert False, "Expected ValueError"
        except ValueError as e:
            assert "Insufficient funds" in str(e)
        assert a.get_balance() == 30.0
        assert b.get_balance() == 5.0

    def test_transfer_zero(self):
        a = BankAccount("A", 20.0)
        b = BankAccount("B", 20.0)
        try:
            a.transfer_to(b, 0.0)
            assert False, "Expected ValueError"
        except ValueError as e:
            assert "Withdrawal must be positive" in str(e)
        assert a.get_balance() == 20.0
        assert b.get_balance() == 20.0

    def test_transfer_neg_amount(self):
        a = BankAccount("A", 50.0)
        b = BankAccount("B", 5.0)
        try:
            a.transfer_to(b, -10.0)
            assert False, "Expected ValueError"
        except ValueError as e:
            assert "Withdrawal must be positive" in str(e)
        assert a.get_balance() == 50.0
        assert b.get_balance() == 5.0

    def test_transfer_to_fake_account(self):
        a = BankAccount("A", 40.0)
        target = object()
        try:
            a.transfer_to(target, 10.0)
            assert False, "Expected ValueError"
        except ValueError as e:
            assert "Transfer target must be a BankAccount" in str(e)
        assert a.get_balance() == 40.0

    def test_double_transactions(self):
        a = BankAccount("A", 90.0)
        b = BankAccount("B", 10.0)
        a.transfer_to(b, 25.0)
        assert a.last_transaction() == ("withdraw", 25.0)
        assert b.last_transaction() == ("deposit", 25.0)
        assert len(a.transactions) == 1
        assert len(b.transactions) == 1

    def test_multiple_ransfers(self):
        a = BankAccount("A", 200.0)
        b = BankAccount("B", 0.0)
        a.transfer_to(b, 50.0) 
        a.transfer_to(b, 25.0)
        a.transfer_to(b, 60.0)
        assert a.get_balance() == 65.0
        assert b.get_balance() == 135.0
        assert a.transactions.count(("withdraw", 50.0)) == 1
        assert a.transactions.count(("withdraw", 25.0)) == 1
        assert a.transactions.count(("withdraw", 60.0)) == 1


    def test_last_interaction_initial(self):
        account = BankAccount("Violet")
        assert account.last_transaction() is None
    
    def test_clear_transaction_history(self):
        account = BankAccount("Fan", 15)
        account.deposit(5)
        account.withdraw(3.0)
        account.clear_transactions()
        assert account.transactions == []
        assert account.last_transaction() is None

    def test_correct_log(self):
        account = BankAccount("Sam")
        account.deposit(10)
        account.deposit(2.5)
        assert account.get_balance() == 12.5
        assert account.transactions[0] == ("deposit", 10)
        assert account.last_transaction() == ("deposit", 2.5)

    
    def test_clear_on_empty_history(self):
        account = BankAccount("A")
        assert account.transactions == []
        assert account.last_transaction() is None
        account.clear_transactions()
        assert account.transactions == []
        assert account.last_transaction() is None