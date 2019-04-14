#
# Banking simulator. Write a code in python that simulates the banking system.
# The program should:
# - be able to create new banks
# - store client information in banks
# - allow for cash input and withdrawal
# - allow for money transfer from client to client
# If you can think of any other features, you can add them.
# This code shoud be runnable with 'python kol1.py'.
# You don't need to use user input, just show me in the script that the structure of your code works.
# If you have spare time you can implement: Command Line Interface, some kind of data storage, or even multiprocessing.
#
# Try to expand your implementation as best as you can.
# Think of as many features as you can, and try implementing them.
# Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
# Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
# The goal of this task is for you to SHOW YOUR BEST python programming skills.
# Impress everyone with your skills, show off with your code.
#
# Your program must be runnable with command "python task.py".
# Show some usecases of your library in the code (print some things)
#
# When you are done upload this code to your github repository.
#
# Delete these comments before commit!
# Good luck.

class Client:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount


class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.client_array = []

    def newClient(self, name, amount=0):
        client = Client(name, amount)
        self.client_array.append(client)

    def cashImput(self, client_name, client_amount):
        for n in self.client_array:
            if n.name == client_name:
                n.amount += int(client_amount)

    def cashOutput(self, client_name, client_amount):
        for n in self.client_array:
            if n.name == client_name:
                if n.amount >= n.amount - int(client_amount):
                    n.amount -= int(client_amount)

    def transfer(self, client1_name, client2_name, client1_amount):
        for n1 in self.client_array:
            if n1.name == client1_name:
                for n2 in self.client_array:
                    if n2.name == client2_name:
                        if n1.amount >= int(client1_amount):
                            n1.amount -= int(client1_amount)

                            n2.amount += int(client1_amount)

                        else:
                            print('not enough money')

    def printAllClients(self):
        for n in self.client_array:
            print('bank: {} \t client: {} \t amount: {}'.format(self.bank_name, n.name, n.amount))
    def printClient(self,client_name):
        for n in self.client_array:
            if n.name == client_name:
                print('bank: {} \t client: {} \t amount: {}'.format(self.bank_name, n.name, n.amount))
            
moldoinkombank = Bank('moldinkombank')
moldoinkombank.newClient('Cata', 99)
moldoinkombank.newClient('Marcel', 99)
moldoinkombank.newClient('Marc444el', 99)
print(moldoinkombank.bank_name)
moldoinkombank.cashImput('Cata', 19999)
moldoinkombank.cashOutput('Cata', 55)
moldoinkombank.printAllClients()
victoriabank = Bank('victoriabank')
victoriabank.newClient('Ion', 1000)
victoriabank.newClient('Vasile', 2000)
victoriabank.printAllClients()

moldoinkombank.transfer('Cata', 'Marc444el', 9999)

moldoinkombank.printAllClients()

victoriabank.transfer('Ion', 'Vasile', 1000)

victoriabank.printAllClients()

victoriabank.printClient('Ion')
