The question is to print the numbers mentioned below without using any conditional statements? The set of numbers are var=01120221011202210112. Is there a way to do the same without using conditional statements ?

x=0
y=1
print("01",end='')
for i in range(18):
    z=(x+y)%3
    print(z,end='')
    x=y
    y=z
