
"x"
# h=open('abc1.txt','x')  # it will not open existing file
# h.write('python world')


"w"
# h=open('abc10.txt','w')      # it will open existing file
# h.write('python developer')

"r"
# with open('abc10.txt','r') as k:   # we cant read and write
#     k.write('java developer')


# j=open('abc10.txt','r')      # it will read only existing files
# d=j.read()
# print(d)


# j=open('assign.py','r')      # it is given the existing file data
# d=j.read()
# print(d)                     # mandatory to close the file
# j.close()


# with open('assign.py','r') as k:       # no need to give close function
#     d=k.read()
#     print(d)

"w"

# k=open('abc10.txt','w')      # it will delete the existing data and give new data
# k.write('java developer')


"a"

# k=open('abc10.txt','a')         # it will add or append the data
# k.write(' python developer')


" seek"
# j=open('abc10.txt','r')
# j.seek(14)                 # seek will print the indexing values
# d=j.read()
# print(d)


"tell"

# j=open('abc10.txt','r')
# j.seek(0)
# print(j.tell())        # tell is used to  check the indexing value

"w+ ==> write and read"

# with open('abc102.txt','w+') as k:
#     k.write('Return the number of characters from the string')
#     k.seek(0)                                                   # without seek it will not give any data because it will read forward positions
#     d=k.read()
#     print(d)

"r+ ==> read and write"

# with open('abc102.txt','r+') as k:
#     d=k.read()
#    #print(d)
#     k.write(' this is r+ mode')
    


"a+ ==>  append and read"

# h=open('abc102.txt','a+')
# h.write(' this is a+ mode')
# h.seek(0)
# d=h.read()
# print(d)


"read() ==> used to read total data"

# with open('file100.txt','w') as k:
#     k.write('this is first line \n this is second line \n this is third line')

" readline() ==> used to read only first line"

# b=open('file100.txt','r')
# d=b.read()
# print(d)
# m=b.readline()
# print(m)
# print(b.readline())
# print(b.readline())

'readlines()==> used to read all data in list'


# with open('file100.txt','r') as k:
#     print(k.readlines())
    
"converting one file to another file"

# n=open('assign.py','r')
# m=open('file102.py','w')
# d=n.read()
# m.write(d)

"  removing file using file handling "

# import os

# if os.path.exists('abc.txt'):
#     os.remove('abc.txt')
# else:
#     print('file not found')


" find length using file handling "

# h=open('abc100.txt','r')
# d=h.read()
# print(len(d))

"find lines by using file handling"

# m=open('anagram.py','r')
# d=m.readlines()
# print(len(d))


" (or)"

m=open('armstrong.py','r')
n=m.readlines()

cou=0
for x in n:
    cou+=1
print(cou)






