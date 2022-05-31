#Question 1
#Using the given list, print out a filtered version of the list with only the numbers that are less than ten
alist = [1,11,14,5,8,9]
nums = [x for x in alist if x < 10]
print(nums)

#Question 2
#Merge and sort the two lists below
#l_1 = [1,2,3,4,5,6]
#l_2 = [3,4,5,6,7,8,10]
l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]

l_3 = l_1 + l_2
l_3.sort()
print(l_3)

#Bonus question 1
#accept two user ages as inputs and give us the difference between the two of them. (the answer should always be a positive output)
x = input("Enter age of first user")
y = input("Enter age of second user")
difference = int(x) - int(y)
print(abs(difference))

#Bonus question 2
#Accept 3 user inputs for variables named "noun" "verb" and "adjective" and print out a formatted string using the outputs.
n = input("Enter a noun")
v = input("Enter a verb")
a = input("Enter an adjective")
print(f"The noun entered was {n}, the verb entered was {v}, and the adjective entered was {a}")

#Bonus question 3
#Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors
age = int(input("Please enter your age"))
if age < 18:
    print("Kids")
elif age >= 18 and age <= 65:
    print("Adults")
else:
    print("Seniors")
