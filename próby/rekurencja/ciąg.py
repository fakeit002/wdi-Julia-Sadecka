
def ciag(x):
    if x <= 1:
        return 1
    else:
        return x + ciag(x-1)


print(ciag(10))