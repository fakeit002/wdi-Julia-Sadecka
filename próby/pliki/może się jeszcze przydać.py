y = tab.index(['.'])
tab1 = []
tab1.append(tab[0:y])
tab2 = []
tab2.append(tab[y + 1:])
for i in range(len(tab1)):
    print(i)
    # for j in range(len(tab1)):
    #     print(j)

print(tab1)
# print(tab2)
