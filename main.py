strpasword = "a123456"
i = 3
while i > 0:
	strinput = input("Please input password")
	if strinput == strpasword:
		print("Correct!!")
		break
	else:
		print("Incorrect, you still can try ", i - 1 ," times!")
		i = i - 1
