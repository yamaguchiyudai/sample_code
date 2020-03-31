import sys
arg = sys.argv
import re
array = []
arr = []
m = 0
lines =  open(arg[1])
for line in lines:
	a = re.split(':', str(line))
	arr.append(tuple(a))
m = arr[-1][0]
arr.pop(-1)
array.append(arr)
def FizzBuzz(a, m):
	text = []
	ar = dict(sorted(dict(a).items()))
	for i, s in ar.items():
		if int(m)%int(i) == 0:
			s.replace("\n", "")
			text.append(str(s))
	if text == []:
		print(m)
	print(''.join(text))
FizzBuzz(array[0], m)