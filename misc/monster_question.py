# 1,000 people are indexed from 1 to 1,000
# A monster comes and eats the odd indexed people
# The remaining people are moved over one spot
# The monster repeats this process until one is left
# What is the original index of the final person?
steps = 0
x = list(range(1,1001))
while(len(x)>1):
	x = x[1::2]
	steps += 1
print("The monster took {} rounds until he finished".format(steps))
print("The final person had index {0}".format(x[0]))