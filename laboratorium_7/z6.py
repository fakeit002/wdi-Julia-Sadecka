
lista = list(input("Wprowadź ciąg znaków: "))
x = lista.index('0')
lista.reverse()
y = lista.index('0')
z = len(lista)
lista.reverse()
lista2 = lista[(x + 1):(z - y - 1)]
print(lista2)

lista3 = []
for i in lista2:
    i = ord(i)
    lista3.append(i)
lista3.sort()
print(lista3)

a = lista3[4]
print(a)
print(chr(a))

# przypadki testowe
# Blsur".<uf0je^#ndji---0Hlk2555
# bfjakeibfuujdjskakdhhb0KSHF63872nfnskjbf0ksjbrfaoohnfhe2549665455545ajhherbf;'?.)9(kshfkall-----=+++++lsjkdfagudDFRHKB0SKJDFBASEBR5327zxbrj}{][fnslr\\\\aljehbenwkandhhbfahrdkh12345678bxzHKSJRHUUHHHJSKFBKSHAKadhfjkskbcubnr????,.;sjf25;ajh653428zxcvbnmasdfghjklqwertyuiop0dbjhsbdjhbk546abdjhkammjabdhekakjadbjfhjajjbzdjhawejuyfdbviau76372jjsdhrifabwbaodfkjakfhLLKJHFFD"}|slab....ahgrv25486970aherfbbbekwkuebsksbJKKKKKKJBHJDKSBFBJAS
# bgh0hjkad0bj0hh0dao