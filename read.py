products = []
while True:
	name = input('輸入商品名稱:')
	if name =='q':
		break
	price = input('輸入商品價格:')
	#products.append([name, price])
	p = []
	p.append(name)
	p.append(price)
	products.append(p)
print(products)
print(products[0][0])