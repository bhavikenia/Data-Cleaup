####################################################################
#                     Code Maker - By: Bhavi Kenia p1              #
#                        Last Revised: 1/17/2022                   #
# This is a program which displays your favorite number in a list. #
# This program uses data cleanup along with converging points. The #
# input is a sett of data values that may contain 0s, although     #
# 0s are considered invalid data. The output is to be a clean set  #
# of data where the 0s have been eliminated. The converging        #
# pointers data cleanup algorithm is the more time and space       #
# efficient.                                                       #
####################################################################



# Get the values for n and the n data items 
n = int(input("How many numbers are in the list: "))
data = [] # create an empty list

i = 0
number = int(input("Enter first favorite number: "))
data.append(number) #append a value to the data list
while i < n - 1:
     i = i + 1
     number = int(input("Enter next favorite number: "))
     data.append(number)

#Set the value of elgit, left, and right 
legit = n - 1
left = 0
right = n - 1

print()
print("The orginal list is")
i = 0
while i <= legit:
    print(data[i],end=" ")
    i = i + 1
print()

#more the pointers together,
#swapping value at right for 0 at left

while left < right:
    if data[left] != 0:
        left = left + 1
    else:
        legit = legit - 1
        data[left] = data[right]
        right = right -1
if data[left] == 0:
    legit = legit - 1

#final output
print("The cleaned list is")
i = 0
while i <= legit:
    print(data[i], end=" ")
    i = i + 1

#finish up 
input("\n\nPress the Enter Key to exit"); 