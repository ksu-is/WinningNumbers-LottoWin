#Lottery Numbers - www.101computing.net/lottery-numbers


#Here I've copied the code from my Visual Studio Code 
import random

#Initialise an empty list that will be used to store the 6 lucky numbers!
lotteryNumbers = []

for i in range (0,6):
  number = random.randint(1,50)
  #Check if this number has already been picked and ...
  while number in lotteryNumbers:
    # ... if it has, pick a new number instead 
    number = random.randint(1,50)
  
  #Now that we have a unique number, let's append it to our list.
  lotteryNumbers.append(number)

#Sort the list in ascending orderr
lotteryNumbers.sort()

#Display the list on screen:
print(">>> Today's lucky lottery numbers are: ") 
print(lotteryNumbers)


print("Have a great day, hope you win!")
