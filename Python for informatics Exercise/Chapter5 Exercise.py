# 5.1
total = 0
count = 0
avg = 0
n= None
while n != "done" :
	try:
		n = raw_input("Enter a number\n")
		total += float(n)
		count+=1
		avg = total/count
	except:
		print "Invalid input"
print total,count,avg

# 5.2
maximum = None
minimum = None
n= None
while n != "done" :
	try:
		n = raw_input("Enter a number\n")
		if maximum == None or maximum < int(n) :
			maximum=int(n)
		if minimum == None or minimum > int(n) :
			minimum=int(n)
	except:
		print "Invalid input"
print maximum,minimum