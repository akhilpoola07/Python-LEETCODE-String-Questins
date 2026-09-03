n = int(input())
sob = []
while n>0:
	sob.append(n%10)
	n//=10
sum = 0
while sob:
	sum += sob.pop()
print(sum)