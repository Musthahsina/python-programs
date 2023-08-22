class Bank:
    def __init__(self, b_name, b_transaction):
        self.name = b_name
        self._trans = b_transaction

    def test(self):
        print('trans', self._trans)
        bank = Bank('SBI', 12345678)
        print(bank._trans)


class Customer(Bank):
    def bank_data(self):
        print(self.name)
        print(self._trans)


obj = Customer('SBI', 45678987654)
obj.bank_data()

"""
"""

class Bank:
    def _init_(self,b_name,b_transaction,b_balance):
        self.name=b_name        # Public mode
        self.trans=b_transaction       # Protected mode ()after self.
        self._bal=b_balance        # Private Mode(_) after self.
    def test(self):
        print("Private mode balance in Parent class:",self.__bal)
class Customer(Bank):
    def bank_data(self):
        print("Bank name:",self.name)       # subclass can access the Public mode data
        print("Transcation:",self._trans)   # subclass can also access Protected mode data
        #print("Balance:",self.__bal)        # shows error because subclass cannod access private mode data
obj=Customer("SIB",12345678,100)
obj.bank_data()     # cannot access private mode attributes with a child class object
bank=Bank("Sib",458897,500)
bank.test()