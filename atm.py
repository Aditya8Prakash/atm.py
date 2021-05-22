class Atm (object):
    def __init__(self,bank, balance ,cardnumber,pin) :
        self.bank = bank
        self.cardnumber = cardnumber
        self.pin = pin
        self.balance = balance

    def cashWithdrawl (self) :

        cardno = input('Enter your card no. : ')
        password = input('Enter your password : ')
        amount = int(input(' Enter your Amount : '))

        if cardno == self.cardnumber :
            if password == self.pin :
                if amount< self.balance:
                    print('withdrawal successful')
                    self.balance = self.balance - amount
                else :
                    print('invalid amount')

            else :
                print('invalid password')

    def BalanceEnquiry (self) :

        cardno = input('Enter your card no. : ')
        password = input('Enter your password : ')

        if cardno == self.cardnumber :
            if password == self.pin :
                print(self.balance)
            else :
                print('invalid password')

atm = Atm('SBI', 15000,10019,1934)

atm.cashWithdrawl()
atm.BalanceEnquiry()