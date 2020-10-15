inx = float(input())
iny = float(input())

if inx > 0:
	if iny > 0:
		print("I")
	else:
		print("IV")
elif inx < 0:
	if iny > 0:
		print("II")
	else:
		print("III")