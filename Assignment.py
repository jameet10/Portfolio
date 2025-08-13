
#For swapping of two numbers
a=10
b=20
print("Before Swapping")
print(a)
print(b)

(a,b) = (b,a)

print("After Swapping")
print(a)
print(b)

#For making pattern


for i in range(1,6):
    for j in range(1,i+1):
        print(j, end="")
    print()
   