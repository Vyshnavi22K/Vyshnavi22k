a=[]
for i in range(1,3):
	x=int(input("enter: "))
	a.append(x)
	print(a)
b=[]
for i in range(1,3):
	y=int(input("enter: "))
	b.append(y)
	print(b)
dot_product=sum(x*y for x,y in zip(a,b))
print("dot_product",dot_product)
