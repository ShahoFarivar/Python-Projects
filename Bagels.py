import random

info='''I am thinking of a 3-digit number. Try to guess what it is.\nThe clues I give are... \n\nWhen I say:    That means:\n   Bagels       None of the digits is correct.\n   Pico         One digit is correct but in the wrong position\n   Fermi        One digit is correct and in the right position.\nI have thought up a number. You have 10 guesses to get it.\n'''

def is_unique(num):
		num_list=to_list(num)
		for item in num_list:
			count=num_list.count(item)
			if count>1:
				return False
		return True		
		
def is_number(num):
			try:
				inp=int(num)
				return True
			except ValueError:
				print("Not a number")
				return False

def is_three_digits(num):
	counter=0
	con=True
	while con:
		num=int(num/10)
		counter+=1
		if num==0:
			con=False
	if counter==3:
		return True
	else:
			print("Not three digits.")
			return False

def to_list(num):
	num_list=[]
	con=True
	while con:
		if num != 0:
			num_list.append(int(num%10))
			num=int(num/10)
		else:
			con=False
	num_list.reverse()
	return num_list

def ai_num():
	numbers=[1,2,3,4,5,6,7,8,9]
	aiNum=[]
	counter=0
	for i in range(3):
		choice=random.choice(numbers)
		aiNum.append(choice)
		numbers.remove(choice)
		if counter<1:
			numbers.append(0)
			counter+=1		
	return aiNum
							
def get_input():
	cond=True
	while cond:
		num=input("Enter a 3 digit number with uinque numbers: ")
		if is_number(num) == True:
			 num=int(num)
			 if is_three_digits(num) == True and is_unique(num):
			 	cond = False
			 	return num
		else:
			 	print("Only enter a three digit number with uniqe numbers.")

def game():
	running=True
	aiNum=ai_num()
	counter=0
	while running and counter<=10:
		result=[]
		result.clear()
		userNum=to_list(get_input())
		print(userNum)
		while len(result)<3:
			result.append("Bagels")
		for i in aiNum:
			for j in userNum:
				if i==j and aiNum.index(i)==userNum.index(j):
					result.remove("Bagels")
					result.append("Fermi")
				elif i==j and aiNum.index(i) != userNum.index(j):
					result.remove("Bagels")
					result.append("Pico")
		random.shuffle(result)
		print(result)
		counter+=1
		print(10-counter, " tries left")
		if counter== 10:
			print("You lost, correct answer is ", aiNum)
			return
		if result.count("Fermi")==3:
			print("You won!")
			return
	
def replay():
	while True:
		answer=input("Do you want to play again? (y/n)")
		if answer == "y":
			return True
		elif answer == "n":
			print("Exiting...")
			return False
		else:
			print("Only enter y or n")

def main():
	running=True
	global info
	print(info)
	while running:
		game()
		running=replay()
		
main()

			 
