# 3.1
hours = int(raw_input("Enter Hours\n"));
rate = float(raw_input("Enter rate\n"));
pay = hours * rate
if hours>40 :
	pay = 1.5 * pay
print pay

#3.2
#using try and except
hours = raw_input("Enter Hours\n");
try :
	hours = int(hours)
	rate = raw_input("Enter rate\n");
	try :
		rate = float(rate)
		pay = hours * rate
		if hours>40 :
			pay = 1.5 * pay
		print pay 
	except:	
		print "Error, please enter numeric input"
except:
	print "Error, please enter numeric input"



#3.3
#score calculator
score = raw_input("Enter score : ");
try:
	score=float(score)
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
	print grade
except:
	print "Bad score"
