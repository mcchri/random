#1
import random
# a = random.randint(1,100)
# print(a)

#2
# fruit = ["Apple","Banana","Orange","Pear","Grape"]
# n = random.randint(0,4)
# print(fruit[n])

#3
# inp = input("h or t")
# n = random.randint(1,2)
# if (inp == "h" and n == 1) || (inp == "t" and n == 2):
#     print("You win")
# else:
#     print("You lose")

#4
# n = random.randint(1,5)
# 
# count = 0
# while count < 2:
#     guess = int(input("Enter a number: "))
#     if guess > n:
#         print("Too high")
#     elif guess < n:
#         print("Too low")
#     elif guess == n:
#         print("Thats correct ")
#         break
#     count +=1
# if count == 2:
#     print("You lose")
    
#5
# n = random.randint(1,10)
# inp = int(input("Enter a number"))
# while inp != n:
#     inp = int(input("Enter a number"))
  
#6
# n = random.randint(1,10)
# inp = int(input("Enter a number"))
# while inp != n:
#     if inp > n:
#         print("Too high")
#     elif inp < n:
#         print("Too low")
#     inp = int(input("Enter a number"))
    
#7
# point = 0
# for i in range(5):
#     n1 = random.randint(1,10)
#     n2 = random.randint(1,10)
#     inp = int(input(f"What is {n1} + {n2} "))
#     if inp == (n1+n2):
#         point += 1
# print(point)

#8
# colours = ["green","yellow","blue","violet","red"]
# for i in colours:
#     print(i)
#     
# n = random.randint(0,4)
# inp = ""
# while inp != colours[n]:
#     inp = input("Enter a colour ")
#     if inp == colours[n]:
#         print("Well done")
#     else:
#         print(f"Wrong, you are too {colours[n]} ")