'''2'''
str = input()
words = list(str.split(' '))
for even in words:
	if( len(even) % 2 == 0 ):
		print(even)


'''3'''
str = input()
l = 0
for s in str:
      l = l + 1
print(l)


'''4'''
def WordPresent(text, word):
	t = text.split(" ")
	for i in t:
		if (i == word):
			return True
	return False
t = input()
word = input()

if (WordPresent(t, word)):
	print("True")
else:
	print("False")


'''5'''
def Replace(str):
	maketrans = str.maketrans
	final = str.translate(maketrans(',.', '.,', ' '))
	return final.replace(',', ', ')

string = input()
print(Replace(string))