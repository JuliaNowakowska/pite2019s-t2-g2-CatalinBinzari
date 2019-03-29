#
#Banking simulator. Write a code in python that simulates the banking system. 
#The program should:
# - be able to create new banks
# - store client information in banks
# - allow for cash input and withdrawal
# - allow for money transfer from client to client
#If you can think of any other features, you can add them.
#This code shoud be runnable with 'python kol1.py'.
#You don't need to use user input, just show me in the script that the structure of your code works.
#If you have spare time you can implement: Command Line Interface, some kind of data storage, or even multiprocessing.
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to your github repository. 
#
#Delete these comments before commit!
#Good luck.

class Bank:
    def __init__(self,bankName,userID,userPD,userAmount):
        self.bankName=bankName
        self.userID=userID
        self.userPD=userPD
        self.userAmount=userAmount
    def cash_imput(self,imput_value):
        self.userAmount=self.userAmount+imput_value
    def cash_output(self,output_value):
        self.userAmount=self.userAmount-output_value
    def user_info(self):
       return 'User:{} \t User amount:{} \t Bank:{} \n'.format(self.userID,self.userAmount,self.bankName)
    #def transfer(self,value,):
     #   if self.userAmount>value:
      #      self.userAmount=self.userAmount-value

        
cata=Bank('Moldinkombank',2344,888,32)
print(cata.user_info())
cata.cash_imput(68)
print(cata.user_info())
cata.cash_output(55)
print(cata.user_info())
mary=Bank('Moldinkombank',1000,100,899)
print(mary.user_info())
#mary.transfer(33,cata.userAmount)
