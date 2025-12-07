" ducttype"

# class India:
#     def national_lang(self):
#         print("india national language is: hindi")
#     def capital(self):
#         print("india capital is:Delhi")
# class America:
#     def national_lang(self):
#         print("America national language is:english")
#     def capital(self):
#         print("America capital is:washington DC")

# def details(value):
#     value.national_lang()
#     value.capital()

# I_obj=India()

# details(I_obj)

# A_obj=America()
# details(A_obj)

"method overloading"  # same function different parameters

# def add1(a,b):
#     return a+b
# def add1(a,b,c):
#     return a+b+c
# def add1(a,b,c,d):
#     return a+b+c+d

# print(add1(10,20,30,40))

"method overiding"   # same functions and same parameters

# def add1(a,b):
#     return a+b
# def add1(a,b):
#     return a+b
# def add1(a,b):
#     return a+b

# print(add1(10,20))

" default arguments"

# class A:
#     def __init__(self,a=None,b=None,c=None,d=None):
#         if a!=None and b!=None and c!=None and d!=None:
#             print(a+b+c+d)
#         elif a!=None and b!=None and c!=None:
#             print(a+b+c)
#         elif a!=None and b!=None:
#             print(a+b)
#         else:
#             print("Enter two values:")

# obj=A(10,20)

# obj2=A('python','developer')

# obj3=A(100,200,300,400)

" variable length argument"

# class B:
#     def method(self,*s):
#         a=0
#         for x in s:
#             a+=x
#         print(a)

# obj=B()
# obj.method(10,20)   

# print()
# obj2=B()
# obj2.method(10)

# print()

# obj3=B()
# obj3.method(10,20,30,40,50,60)


b=1000

c='python'

a=7000
