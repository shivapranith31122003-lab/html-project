" single inheritance"   # one child class is inherits from one parent

# class parent:
#     def method(self):
#         print("This is parent class")
# class child(parent):
#     def method2(self):
#         print("This is child class")

# obj=child()
# obj.method()   #parent
# obj.method2()  #child

"  "
# class parent:
#     def __init__(self):
#         self.f_name='ramesh'
#         self.f_age=45
# class child(parent):
#     def details(self):
#         self.name='shiva'
#         self.age=22

#         print("Father name:",self.f_name)
#         print("Father age:",self.f_age)
#         print()
#         print("child name:",self.name)
#         print("child age:",self.age)

# # obj=parent()
# # print(obj.f_name)
# # print(obj.f_age)

# obj2=child()
# obj2.details()
# print()
# print(obj2.f_name)
# print(obj2.f_age)
# print(obj2.name)
# print(obj2.age)


"constructor overidng"

# class parent:
#     def __init__(self):
#         self.name='hari'
#         print("parent name:",self.name)
# class child(parent):
#     def __init__(self):
#         self.child_age=21
#         super().__init__()
#         print('child age:',self.child_age)
# obj=child()


"method overiding"
# class parent:
#     def method(self):
#         self.f_name='ramesh'

# class child(parent):
#     def method(self):
#         self.child_name='pranith'
#         super().method()
#         print('child name:',self.child_name)
#         print('father name:',self.f_name)

# obj=child()
# obj.method()

# class parent:
#     def method(self,f_name):
#         self.father_name=f_name

# class child(parent):
#     def method(self,f_name,c_name):
#         self.child_name=c_name
#         super().method(f_name)

#         print('child name:',self.child_name)

#         print('father name:',self.father_name)
        
# obj=child()
# obj.method('ravi','kumar')


# class parent:
#     def __init__(self,f_name):
#         self.father_name=f_name

# class child(parent):
#     def __init__(self, f_name,c_name):
#         super().__init__(f_name)
#         self.child_name=c_name

#         print('child name:',self.child_name)

#         print('father name:',self.father_name)
        
# obj=child('ravi','kumar')


"multiple inheritance"   # one child class inherits from more than one parent class

# class parent1:
#     def method1(self):
#         print("This is parent1")
# class parent2:
#     def method2(self):
#         print("this is parent2")
# class child(parent1,parent2):
#     def method3(self):
#         print("this is child")

# obj=child()
# obj.method1()
# obj.method2()
# obj.method3()


# class parent1:
#    def __init__(self):
#       print('this is parent1 class')
# class parent2:
#    def __init__(self):
#       super().__init__()
#       print("this is parent2 class")
# class child(parent1,parent2):
#    def __init__(self):
#       super().__init__()
#       print("this is child class")

# obj=child()



"mutilevel inheritance"    # one grand father inherit from one parent class and one parent class is inherit from child class


# class parent:
#     def method(self):
#         print("10k coders")
# class child(parent):
#     def method(self):
#      super().method()
#      print('fullstack python')
# class A(child):
#      def method(self):
#          super().method()
#          print("python")
# obj=A()
# obj.method



# class g_parent:
#    def __init__(self):
#       print("This is grand parent class")
# class parent(g_parent):
#    def __init__(self):
#       super().__init__()
#       print("This is parent class")
# class child(parent):
#    def __init__(self):
#       super().__init__()
#       print("this is child class")

# obj=child()


"Hierarchical inheriatnce "   # one parent class is inherit from more than one child class

# class parent:
#     def method1(self):
#         print("This is parent class")
# class child1(parent):
#     def method2(self):
#         print("This is child1 class")
# class child2(parent):
#     def method3(self):
#         print("This is child2 class")
# class child3(parent):
#     def method4(self):
#         print("This is child3 class")

# obj=child3()
# obj.method4()
# obj.method1()

# print()

# obj2=child2()
# obj2.method3()
# obj2.method1()

# print()

# obj3=child1()
# obj3.method2()
# obj3.method1()


"Hybrid inheriatnce"   # combination of more than one inheriatnce is called hybrid 

# class grand_father():
#     def method1(self):
#         print("This is grand father class")
# class parent1(grand_father):
#     def method2(self):
#         print("This is parent one class")
# class parent2(grand_father):
#     def method3(self):
#         print("This is parent two class")
# class child(parent1,parent2):
#     def method4(self):
#         print("This is child class")

# obj=child()
# obj.method1()
# obj.method2()
# obj.method3()
# obj.method4()


"Abstraction"  # it is used to hide the internal process and show only features of the object to the user.

" concrete class" # concrete class is a regular class that has complete code for all its methods and can create objects.

# from abc import ABC,abstractmethod                 # abc means abstraction base class
#                                                    # we cant create object to this abstraction
# class Bank(ABC):
#     @abstractmethod
#     def create_acc(self):
#         pass
#     @abstractmethod
#     def deposit(self):
#         pass
#     @abstractmethod
#     def withraw(self):
#         pass
#     @abstractmethod
#     def check_balance(self):
#         pass


# class union(Bank):                         # concrete class
#     def create_acc(self):
#         print("create account")
#     def deposit(self):
#         print("deposit")
#     def withraw(self):
#         print("withdraw")
#     def check_balance(self):
#         print("balance")

# obj=union()
# obj.create_acc()
# obj.deposit()
# obj.withraw()
# obj.check_balance()


# from abc import ABC,abstractmethod                 # abc means abstraction base class
#                                                    # we cant create object to this abstraction
# class Bank(ABC):
#     @abstractmethod
#     def create_acc(self):
#         pass
#     @abstractmethod
#     def deposit(self):
#         pass
#     @abstractmethod
#     def withraw(self):
#         pass
#     @abstractmethod
#     def check_balance(self):
#         pass


# class union(Bank):
#     def create_acc(self,A_cno,balance):
#         self.account_number=A_cno
#         self.balance=balance
#         print("your account is created")
#     def deposit(self,account_no,D_amount):
#         if self.account_number==account_no:
#             self.balance+=D_amount
#             print("Total Balance:",self.balance)
       
#     def withraw(self,Acc_no,w_amount):
#         if Acc_no==self.account_number and self.balance>w_amount:
#             self.balance-=w_amount
#             print("After withdraw: balance",self.balance)
#     def check_balance(self,Ac_cno):
#         if Ac_cno==self.account_number:
#             print("balance:",self.balance)

# obj=union()
# obj.create_acc(101,5000)
# obj.deposit(101,3000)
# obj.withraw(101,4000)
# obj.check_balance(101)
    
    
    
"  "

# from abc import ABC,abstractmethod

# import random

# class Bank(ABC):
#     @abstractmethod
#     def create_account(self):
#         pass
#     @abstractmethod
#     def deposit(self):
#         pass
#     @abstractmethod
#     def withdraw(self):
#         pass
#     @abstractmethod
#     def details(self):
#         pass
# class union(Bank):
#     def create_account(self):
#         self.holder_name=input("Enter holder name:")
#         self.mobile=int(input("Enter your mobile:"))
#         self.Account_number=random.randint(00000000000,99999999999)
#         self.balance=1000
#         self.IFSC_CODE='IFSC0100'
        
#         print("Account_number:",self.Account_number)
#         print("your account number created successfully ")

#     def deposit(self):
#         self.Acc_no=int(input("Enter your account number:"))
#         self.D_amount=int(input("Enter your deposit amount:"))
#         if self.Acc_no==self.Account_number:
#             self.balance+=self.D_amount
#             print("deposit amount:",self.balance)

#     def withdraw(self):
#         self.acc_no=int(input("Enter your account number"))
#         self.w_amount=int(input("Enter your withdraw amount:"))

#         if self.acc_no==self.Account_number and self.balance>self.w_amount:
#             self.balance-=self.w_amount
#             print("withdraw amount:",self.balance)
#     def details(self):
#         self.Acc_No=int(input("Enter your account number:"))
#         if self.Acc_No==self.Account_number:
#             print("name:",self.holder_name)
#             print("mobile:",self.mobile)
#             print("balance:",self.balance)
#             print("IFSC:",self.IFSC_CODE)
# obj=union()
# while True:
#     print(""" 
#                Enter 1==>create account
#                Enter 2==> deposit
#                Enter 3 ==> withdraw
#                Enter 4==>details
#                Enter 5 ==> exit""")
#     n=int(input("Enter your option:"))
#     if n==1:
#         obj.create_account()
#     elif n==2:
#         obj.deposit()
#     elif n==3:
#         obj.withdraw()
#     elif n==4:
#         obj.details()
#     elif n==5:
#         break


" "
from abc import ABC,abstractmethod

class vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def stop_engine(self):
        pass
    # @abstractmethod
    def fuel_status(self):
        print("fuel level is good")

class car(vehicle):
    def start_engine(self):
        print("car engine started")
    def stop_engine(self):
        print("car engine stopped")

class bike(vehicle):
    def start_engine(self):
        print("bike engine started")
    def stop_engine(self):
        print("bike engine stopped")

obj=car()
obj2=bike()


print("----car----")

obj.start_engine()
obj.fuel_status()
obj.stop_engine()


print("---bike---")

obj2.start_engine()
obj2.stop_engine()
obj2.fuel_status()
        
    



    



    

    
    

     
    





