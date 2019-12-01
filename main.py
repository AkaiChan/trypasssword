strpasword = "a123456"
i = 3
while i > 0:
	i = i - 1
	strinput = input("Please input password: ")
	if strinput == strpasword:
		print("Correct!!")
		break
	else:
		print("Incorrect")
		if i > 0: 
			print("you still can try ", i ," times!")
		else:
			print("Account is locked")

