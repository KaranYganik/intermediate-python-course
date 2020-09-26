import random
def main(min,max):
	while True:
		print ("Rolling the dices...")
		print ("The values are....")
		print (random.randint(min, max))
			
		roll_again = input("Roll the dices again?")
		roll_againn = roll_again.lower()
		if roll_againn == 'no' or roll_againn =='n':
			break

if __name__== "__main__":
  main(1,6)
