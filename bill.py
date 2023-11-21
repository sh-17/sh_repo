products = ["Cello pen","Parker","Marker","Eraser","Files"]
price = [50,250,25,10,50]
quantity = [100,50,20,10,50]
sum = 0
index = 0
for i in range(0,len(products)):
    print(products[i],'--',quantity[i],'--',price[i],'Total:',quantity[i]*price[i])
    sum = sum+(quantity[i]*price[i])
print("Grand total:",sum)

#scripts - Search product and display price of it.
'''search = input("Enter product name:")
for i in range(0,len(products)):
    if search == products[i]:
        print("Price of the product is:",price[i])
        break
else:
    print("Product not found")'''

#name of product : Lowest price
'''low = price[0]
for i in range(0,len(products)):
    if low > price[i]:
        low = price[i]
        index = i
print("chepest product is :",products[index])'''

#A-Z
sortedproducts = sorted(products)
print(sortedproducts)
for i in sortedproducts:
    for j in range(0,len(products)):
        if i == products[j]:
            print('product',i,'price:',price[j],'quantity is :',quantity[j],'total:',price[j]*quantity[j])
total = price[j]*quantity[j]

