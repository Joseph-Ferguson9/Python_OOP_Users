class USER:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print(f"{self.name}'s current account balance is ${self.account_balance}.")
    def transfer_money(self, other_user, amount):
        other_user.account_balance += amount
        self.account_balance -= amount
joseph = USER("Joe Ferguson", "joegferguson@gmail.com")
rydder = USER("Rydder Green", "rydderG@gmail.com")
derek = USER("Derek Canoli", "thegodfather@gmail.com")

joseph.make_deposit(1400)
joseph.make_deposit(55)
joseph.make_deposit(800)
joseph.make_withdrawal(700)
joseph.display_user_balance()

rydder.make_deposit(1400)
rydder.make_deposit(500)
rydder.make_withdrawal(3000)
rydder.make_withdrawal(20)
rydder.display_user_balance()

derek.make_deposit(1400)
derek.make_withdrawal(300)
derek.make_withdrawal(100)
derek.make_withdrawal(400)
derek.display_user_balance()

joseph.transfer_money(rydder, 1120)
derek. transfer_money(rydder, 50)

joseph.display_user_balance()
rydder.display_user_balance()
derek.display_user_balance()