#Imports
import time

#variables
scoreall = 0

def test_1(marks):
	global scoreall
	score = scoreall
	answer = ("")
	print ("What does  mean??")
	print ("A. ")
	print ("A. ")
	print ("A. ")
	print ("A. ")
	usr = input('>>>')
	if usr == answer:
		score = scoreall + marks
		return score

def test_2(marks):
	global scoreall
	score = scoreall
	answer = ("")
	print ("What does  mean??")
	print ("B. ")
	print ("B. ")
	print ("B. ")
	print ("B. ")
	usr = input('>>>')
	if usr == answer:
		score = scoreall + marks
		return score

scoreall = test_1(1)
print (scoreall)
scoreall = test_2(1)
print (scoreall)

