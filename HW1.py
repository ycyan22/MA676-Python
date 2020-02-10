# =============================================================================
# MA 676 Python 
# Assignment 1
# Yichu Yan
# =============================================================================


#Problem 1
#a
a = list(range(1,21,1))
print(a)
    
#b
b = list(range(20,0,-1))
print(b)

#c
c = list(range(1,20,1)) + list(range(20,0,-1))
print(c)

#d
d = 10*[4,6,3]
print(d)

#e
e = 11*[4,6,3] 
del e[-2:]
print(e)



#Problem 2
import math
import numpy as np
n = np.arange(3,6.1,0.1)

newlist = []
for i in n:
    funci = math.exp(i) * math.cos(i)
    newlist.append(funci)
print(newlist)



#Problem 3
a = list(range(1,26,1))
newlist2 = []
for i in a:
    funci = 2 ** i / i
    newlist2.append(funci)
print(newlist2)



#Problem 4
#a
list1 = list(range(1,21,1))
list2 = list(range(20,0,-1))
a = [a_i - b_i for a_i, b_i in zip(list1, list2)]
print(a)


#b
a = list(range(1,21,1))
result = []
for i in a:
    if i % 2 == 0:
        result.append('True')
    else:
        result.append('False')
print(result)



#Problem 5
#a
# read txt file
f = open('lorem.txt','r') 
data = f.read()
# delete blank list
lines = data.split("\n\n")

def listToString(s): 
    str1 = " " 
    return (str1.join(s)) 

# split into words   
words = listToString(lines)

lengh1to4=[]
lengh4to7=[]
lengh8=[]   

# set logistic statement to count length    
str_vals = words.split()
for one_str in str_vals:
    length = len(one_str) 
    if length >= 1 and length <= 4:
        lengh1to4.append(length)
for one_str in str_vals:
    length = len(one_str) 
    if length > 4 and length <= 7:
            lengh4to7.append(length)
for one_str in str_vals:
    length = len(one_str) 
    if length >= 8:
        lengh8.append(length)
                
# print answers
print('Number of strings whose lengths is 1-4 = %s' % (len(lengh1to4),))
print('Number of strings whose lengths is 4-7 = %s' % (len(lengh4to7),))        
print('Number of strings whose lengths is 8 or greater = %s' % (len(lengh8),))




#b
print("Capital Letters: ", sum(1 for c in words if c.isupper()))



