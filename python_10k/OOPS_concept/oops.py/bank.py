import random
class Bank:
     total_holders=[]
     def create_account(self):
         details={}
         details['holder_name']=input("Enter holder name:")
         details['aadhar']=int(input("Enter aadhar number:"))
         details['mobile']=int(input("Enter mobile number:"))
         details['IFSCSCODE']='SBIN0990'
         details['Account_number']=random.randint(00000000000,99999999999)
         n=input("Select your account type zero/saving:").lower()
         while True:
             if n=='zero':
                 value=int(input(" your account is zero you have to deposit 500:"))
                 if value>=500:
                     details['balance']=value
                     break
                 else:
                     print("deposit 500 rupees")
             elif n=='saving':
                 value1=int(input("your account is saving you have to deposit 1000:"))
                 if value1>=1000:
                     details['balance']=value1
                     break
                 else:
                     print("deposit 1000 rupees")
             else:
                 print("valid account type")
         Bank.total_holders.append(details)
         print(Bank.total_holders)
obj=Bank()
obj.create_account()