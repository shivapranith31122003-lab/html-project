  
" banking application"

# import random
# class Bank:
#     holder_details=[]
#     def create_account(self):
#         details={}
#         details['holder_name']=input("Enter holder name:")
#         details['mobile_number']=int(input("Enter your mobile:"))
#         details['aadhar']=input("Enter your aadhar number:")
#         details['IFSCCODE']='SBINO110'
#         details['Account_number']=random.randint(111111111111,999999999999)

#         n=input('Select your account type zero/saving:').lower()
#         while True:
#             if n=='zero':
#                 n1=int(input("your account is zero you have to deposit 500 rupees:"))
#                 if n1>=500:
#                     details['balance']=n1
#                     break
#                 else:
#                     print('deposit 500 rupees:')
#             elif n=='saving':
#                 n2=int(input("your account is saving you have to deposit 1000 rupees:"))
#                 if n2>=1000:
#                     details['balance']=n2
#                     break
#                 else:
#                     print("deposit 1000 rupees")
#         Bank.holder_details.append(details)
#         print(Bank.holder_details)
#     def deposit(self):

#             t1=input("enter holder name:")
#             t2=int(input("Enter account number:"))
#             D_amount=int(input("Enter deposit amount:"))

#             for x in Bank.holder_details:
#                 if x['Account_number']==t2 and x['holder_name']==t1:
#                     x['balance']+=D_amount
#                     print("your balance:",x['balance'])
#                     print(x)
#                 else:
#                     print("Enter valid details:")
#     def withdraw(self):

#             r1=input("enter holder name:")
#             r2=int(input("Enter account number:"))
#             w_amount=int(input("Enter withdraw amount:"))

#             for x in Bank.holder_details:
#                 if x['holder_name']==r1 and x['Account_number']==r2:
#                     if x['balance']>=w_amount:
#                         x['balance']-=w_amount
#                         print("your balance:",x['balance'])
#                         print(x)
#                 else:
#                     print("enter valid details")

#     def user_details(self):
#         m1=int(input("Enter account number:"))
#         for x in Bank.holder_details:
#             if x['Account_number']==m1:
#                 for a,b in x.items():
#                     print(a,'===:',b)


# obj=Bank()

# while True:
#     print('''====Bank menu====\n
#          1)create account
#          2) deposit
#          3)withdraw
#          4) user_details
#          5) exit''')
#     n3=input('Select options:')
#     if n3=='1':
#         obj.create_account()
#     elif n3=='2':
#         obj.deposit()
#     elif n3=='3':
#         obj.withdraw()
#     elif n3=='4':
#         obj.user_details()
#     elif n3=='5':
#         break





    
        
        
            
    

