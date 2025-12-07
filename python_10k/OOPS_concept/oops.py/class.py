# def fun():
#     global name,pin,age
#     name='pranith'
#     pin=101
#     age='21'
# def details():
#     global pin
#     pin+=100
#     print(name)
#     print(pin)
#     print(age)
# fun()
# details()

"oops"

# def even():
#     for x in range(10,20):
#         if x%2==0:
#             print(x)
# even()

# for x in range(10,20):
#     if x%2==0:
#         print(x)


"by using oops concept"

# class even():
#     def method(self):
#         for x in range(10,20):
#             if x%2==0:
#                 print(x)
# obj=even()
# obj.method()


# class first():

#     def __init__(self):    # constructor will call automatically
#         print("This is constructor")

#     def method(self):      
#         print("This is method")     # method will not call automatically
# obj=first()
# obj.method()

" constructor"

# class student:
#     def __init__(self):
#         self.name='pranith'
#         print(self.name)
# obj=student()

" method"

# class student():
#     def method(self):
#         self.name='pranith'
#         print(self.name)
# obj=student()
# obj.method()

# class student():
#     def __init__(self):
#         self.name='pranith'
#         self.pin=101
#         self.age=21
#     def details(self):
#         self.mobile=9392648932
#         print(self.name)
#         print(self.pin)
#         print(self.age)
# obj=student()
# obj.details()
# obj.father_name='ramesh'
# print(obj.__dict__)



# class student():
#     def __init__(self,name,pin,age):
#         self.name=name
#         self.pin=pin
#         self.age=age
#     def method(self):
#         print(self.name)
#         print(self.pin)
#         print(self.age)
# obj=student('pranith',201,22)
# obj.method()


# print()
# print('object two:')
# obj2=student('shiva',202,21)
# obj2.method()


# print()
# print("object three")
# obj3=student('siddu',102,18)
# obj3.method()

" "

# class employee():
#     def __init__(self,emp_name,emp_id,emp_salary):
#         print(emp_name)
#         print(emp_id)
#         print(emp_salary)
# obj=employee('shivapraneeth',205,35000)

# class student():
#     def __init__(self):
#         self.school_name='pragna'
#     def details(self,name,pin,f_name,fees,mobile):
#         self.name=name
#         self.pin=pin
#         self.f_name=f_name
#         self.fees=fees
#         self.mobile=mobile
#     def method2(self):
#         print(self.name)
#         print(self.pin)
#         print(self.f_name)
#         print(self.fees)
#         print(self.mobile)
# obj=student()
# obj.details('shivapraneeth',105,'ramesh',30000,9392459087)
# obj.method2()

" "

# class student:
#     def method(self):
#         print("This is instance method")
# obj=student()
# obj.method()

" 1) defining or declaration ==> instance variable"

# class student:
#     def __init__(self):    # parameterless constructor
#         name='pranith'       
#         print(name)

# obj=student()

# class student:
#     def __init__(self,name,pin):    #parameterized
#         name1=name
#         pin1=pin
#         print(f' student name {name1} student pin {pin1}')
# obj=student('pranith',101)

# obj2=student('shiva',102)


"inside constructor"

# class employee:
#     def __init__(self):
#         self.employee_name='pranith'
#         self.employee_id='101'
#         self.employee_salary=35000
#     def method(self):
#         self.f_name='ramesh'
#         self.depart='HR'
#         self.add='hyderabad'
# obj=employee()
# obj.method()
# obj.M_name='sumalatha'
# print(obj.__dict__)

"2)printing ==> "

# class employee:
#     def __init__(self):
#         self.emp_name='shiva'   # instance variable
#         self.emp_pin=103
#         self.emp_salary=30000 
#     # def method(self):
#     #     self.emp_salary=30000    # instance variable

#         print(f'''employee name {self.emp_name}\nemployee id {self.emp_pin}''')

#     def method2(self):
#         print(self.emp_salary)    

# obj=employee()
# # obj.method()
# print(obj.emp_name)
# print(obj.emp_pin)
# print(obj.emp_salary)
# # obj.method2()


# class student:
#     def method(self,name,pin):
#         self.name=name
#         self.pin=pin

#         print(self.name)
#         print(self.pin)

# obj=student()
# obj.method('shiva',105)

# print('=====')

# obj2=student()
# obj2.method('siddu',205)

# print()
# print(obj2.name)
# print()
# print(obj2.pin)
# print()
# print(obj.name)
# print()
# print(obj.pin)



" 3)deleting"

class student:
    def method(self,name,pin):
        self.name=name
        self.pin=pin

    def details(self):
        print('student name:',self.name)

        # del self.pin

        print(self.pin)
        del self.pin

obj=student()
obj.method('shiva',302)
print(obj.pin)
del obj
obj.details()




