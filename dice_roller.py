'''
import random
def main(min,max):
	while True:
		print ("Rolling the dices...")
		print(f"Your number is {random.randint(min, max)}")	
		roll_again = input("Roll the dices again?")
		roll_againn = roll_again.lower()
		if roll_againn == 'no' or roll_againn =='n':
			break

if __name__== "__main__":
  main(1,6)

import random
def roll(min,max):
	while True:
		print ("Rolling the dices...")
		print(f"Your number is {random.randint(min, max)}")	
		roll_again = input("Roll the dices again?")
		roll_againn = roll_again.lower()
		if roll_againn == 'no' or roll_againn == 'n':
			break

if __name__== "__main__":
  roll(1,6)
'''
import random

def roll(min, max):
    while True: 
        print("Rolling the dices...")
        print(f"Your number is {random.randint(min, max)}")
        answer = input("Do you want to roll the dices again? (y/n) ")
        if answer.lower() == "n":
            break

roll(1, 6)
