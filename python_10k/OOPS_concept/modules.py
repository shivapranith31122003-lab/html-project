#help('modules')


# import random

# for x in range(10):
#     print(random.random())



" predefined modules"

# import random
# for x in range(10):
#     print(random.randint(10,20))


# import random

# for x in range(10):
#     print(random.uniform(10,20))

# import random
# print(random.choice(['a','b','c','d','e']))
# print(random.choice('pranith'))

# import random
# for x in range(10):
#     print(random.randint(6000000000,9000000000))


# import random

# h='abcdefghijklmnopqrstuvwxyz'
# r=random.choice(h)
# print(r)

# g=random.choices(h,k=10)
# print(g)
# g=random.choices(h,k=30)      # it won't give any error
# print(g)

# g=random.sample(h,k=10)
# print(g)
# g1=random.sample(h,k=30)     # it will error
# print(g)


# random.seed(10)
# print(random.random())           # it will give constant value


# j=[1,2,3,4]
# print(random.shuffle(j))

# random.shuffle(j)
# print(j)



# password creation

" "
# import random


# a='abcdefghijklmnopqrstuvwxyz'
# b='0123456789'
# c='!@#$%&*^'

# n1=int(input("select number of Alphabets:"))
# n2=int(input("select number of digits:"))
# n3=int(input("select number of special characters:"))

# PASSWORD=''


# for x in range(n1):
#     d=random.choice(a)
#     PASSWORD+=d
# for y in range(n2):
#     d1=random.choice(b)
#     PASSWORD+=d1
# for z in range(n3):
#     d2=random.choice(c)
#     PASSWORD+=d2

# print('your password:',PASSWORD)


#(or)
" "

# import random


# a='abcdefghijklmnopqrstuvwxyz'
# b='0123456789'
# c='!@#$%&*^'

# n1=int(input("select number of Alphabets:"))
# n2=int(input("select number of digits:"))
# n3=int(input("select number of special characters:"))

# m=random.choices(a,k=n1)
# n=random.choices(b,k=n2)
# l=random.choices(c,k=n3)
# res=m+n+l
# print("".join(res))


" "

# import random
# p1=0
# p2=0

# while True:
#     n1=input("p1 press Enter:")
#     if n1=="":
#         d=random.randint(1,15)
#         p1+=d
#         if p1>=20:
#             print(' p1 win score:',p1)
#             break
#     n2=input("p2 press Enter:")
#     if n2=='':
#         d=random.randint(15,20)
#         p2+=d
#         if p2>=20:
#             print('p2 win score:',p2)
#             break


# "pyttsx3"  # pip install pyttsx3

# import pyttsx3

# a=pyttsx3.init()

# a.say('good morning shivapraneeth')

# a.runAndWait()

" "

# import pyttsx3

# a=pyttsx3.init()

# voices=a.getProperty('voices')
# a.setProperty('voice',voices[0].id)    # 0 is for male  and 1 is for female

# a.setProperty('rate',10)

# a.say('good morning ramesh')

# a.runAndWait() 

" "

# import pyttsx3
# import time

# e=pyttsx3.init()

# e.setProperty('rate',100)

# l=['pranith','siddu','shiva','ramesh']
# for y in l:
#     time.sleep(2)
#     e.say(y)
#     e.runAndWait()


# import pyttsx3

# e=pyttsx3.init()


# students=['pranith','shiva','siddu','ramesh']

# attendences={}

# def speak(text):
#     e.say()
#     e.runAndWait()

# for x in students:
#     speak(f'{x}')
#     status=input(f"Is {x} present? (present/p for present,any key for absent):").strip().lower()


#  " "
# from polymorpism import b,a,c
# print(b)
# print(a)
# print(c)

# print( )

# import polymorpism

# print(polymorpism.b)
# print(polymorpism.a)
# print(polymorpism.c)


"data time module"

# import datetime

# current_time = datetime.datetime.now()
# print(current_time)

# "or"

# from datetime import datetime

# current_time=datetime.now()
# print(current_time)

# print()
# d=current_time.date()
# print(d)

# print('year:',d.year)
# print("month:",d.month)
# print("day:",d.day)

# print()
# b=current_time.time()
# print(b)

# print("hour:",b.hour)
# print('minutes:',b.minute)
# print("seconds:",b.second)




# from datetime import datetime,timedelta

# current_time=datetime.now()

# tomorrow=current_time+timedelta(days=3)
# tomorrow1=tomorrow-timedelta(days=3)

# print(tomorrow)
# print(tomorrow1)

" "

# from datetime import datetime

# today='15:30'

# time_12=datetime.strptime(today,'%H:%M').strftime("%I:%M %p")
# print(time_12)

"   clock alram time"

# import datetime

# import time

# import pyttsx3

# engine=pyttsx3.init()

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# alarm_time=input("Enter alarm time in HH:MM:SS format (24-hour): ")

# speak(f"alarm set for {alarm_time}")

# print("alarm set.....")

# while True:
#     current_time=datetime.datetime.now().strftime("%H:%M:%S")

#     if current_time==alarm_time:
#         print("wake up")
#         speak("wake up! your alarm is ringing!")
#         break
#     time.sleep(1)


" "

import pyttsx3

from datetime import datetime

d=pyttsx3.init()

set_time='12:44'

while True:
    present_time= datetime.now().strftime('%H:%M')
    if present_time==set_time:
        for x in range(5):
            d.setProperty('rate',120)
            voices=d.getProperty('voices')
            d.setProperty('voice',voices[1].id)
            d.say('good morning')
            d.runAndWait()
        break
