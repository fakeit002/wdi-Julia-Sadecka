try:
	a = 2
	b = 1
	if b == 1:
		raise RuntimeError
	print(a/b)
except RuntimeError:
	print("UWAGA: nie można dzielić przez zero")
