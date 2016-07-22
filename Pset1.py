s = "alsdf"
def vowel_count(s):
	vowels = ['a','e','i','o','u']
	vowel_count = 0
	for l in s: 
		if l in vowels:
			vowel_count+=1
	print vowel_count 

def bob_count(s):
	bob_count = 0
	for l in range(len(s)): 
		if s[l:l+3] == 'bob':
			bob_count+=1
	print "Number of times bob occurs is: " + str(bob_count)

print bob_count('boblhobootnntbobbcboobobvbor')

def item_order(s):
	s = s + " "
	salad = 0
	water = 0
	hamburger = 0
	index = 0
	while index < len(s):
		if s[index] == 's':
			salad+=1
			index+=6
		elif s[index] == 'w':
			water+=1
			index+=6
		elif s[index] == 'h':
			hamburger+=1
			index+=10
	return "salad:" + str(salad) + " hamburger:" + str(hamburger) + " water:" + str(water)

item_order("salad water hamburger salad hamburger")


	