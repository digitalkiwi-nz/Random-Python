num_of_fibs = raw_input("How many fibs do you want? ")
fibs = []
num1 = 0
num2 = 1
newnum = 1
try:
    num_of_fibs = int(num_of_fibs)
except:
    print "You must enter an integer"

for i in range(num_of_fibs):
    fibs.append(newnum)
    newnum = num1 + num2
    num1 = num2
    num2 = newnum

for fib in fibs:
    print fib