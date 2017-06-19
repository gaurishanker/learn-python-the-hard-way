#chapter 4 Exercise Solutions
# 4.1
import random

for i in range(10) :
	x = random.random()
	print x

# 4.2,4.3

def repeat_lyrics() :
	print_lyrics()
	print_lyrics()
def print_lyrics() :
	print "I'm a lumberjack and I'm Okay"
	print "I sleep all night and I work all day."
repeat_lyrics()

#4.6
def overtime(hours,rate) :
	pay = hours * rate
	if hours>40 :
		pay = 1.5 * pay
	return pay

hours = raw_input("Enter Hours\n");
try :
	hours = int(hours)
	rate = raw_input("Enter rate\n");
	try :
		rate = float(rate)
		print overtime(hours,rate) 
	except:	
		print "Error, please enter numeric input"
except:
	print "Error, please enter numeric input"



#4.7
#score calculator

def score_calculator(score) :
	if score<=1.0 :
		if score>=0.9 :
			grade = "A"
		elif score >= 0.8 :
			grade = "B"
		elif score >= 0.7 :
			grade = "C"
		elif score >= 0.6 :
			grade = "D"
		elif score < 0.6 and score > 0.0:
			grade = "F"
	else :
		grade = "Bad score"
	return grade

score = raw_input("Enter score : ");
try:
	score=float(score)
	print score_calculator(score)
except:
	print "Bad score"
