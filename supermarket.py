#=================================    AUTHOR :-  PRERAK SEMWAL     =====================================
#-------------------------------------------------------------------------------------------------------


dict={0:['Tshirt','Apparels',500],1:['Trousers','Apparels',600],2:['scarf','Apparels',250],3:['Smartphone','Electronics',20000],4:['iPad','Electronics',30000],5:['Laptop','Electronics',50000],6:['Eggs','Eatables',5],7:['Chocolate','Eatables',10],8:['Juice','Eatables',100],9:['Milk','Eatables',45]}

#########################################################################################

def show_menu():
	for i in range(50):
		print("=",end="")
	print("\n\t\t MY BAZAAR")
	for i in range(50):
		print("=",end="")
	print("""\nHello! Welcome to my grocery store!                                                      
Following are the products available in the shop:

-------------------------------------------------                              
CODE | DESCRIPTION |   CATEGORY   | COST (Rs)
-------------------------------------------------
""")
	for i in range(len(dict)):
		s1=" "*(12-len(dict[i][0]))
		s2=" "*(11-len(dict[i][1]))
		print(i,"    | ",dict[i][0],s1,"|   ",dict[i][1],s2,"| ",dict[i][2],sep="")

########################################################################################

def get_regular_input():
	print("""\n\n-------------------------------------------------
ENTER ITEMS YOU WISH TO BUY
-------------------------------------------------
""")
	code_list=[0]*10
	codes=input("Enter the item codes (space-separated): ").split()
	count=0
	for i in range(10):
		code_list[i]=codes.count(str(i))
		count+=codes.count(str(i))
	if count!=len(codes):
		print("NOTE: Invalid input/s discarded !")
	return code_list

########################################################################################

def get_bulk_input():
	print("""\n\n-------------------------------------------------
ENTER ITEM AND QUANTITIES
-------------------------------------------------""")
	code_list=[0]*10
	while True:
		print("Enter code and quantity (leave blank to stop): ",end="")
		vals=input().split()
		if len(vals)==0:
			print("your order has been finalized!")
			break
		if len(vals)!=2:
			print("Invalid number of inputs!")
			continue
		if int(vals[0]) in dict and int(vals[1])>=0:
			code_list[int(vals[0])]+=int(vals[1])
		else:
			if int(vals[0]) not in dict and int(vals[1])<0:
				print("invalid code and quantity. Try Again")
				continue
			if int(vals[0]) not in dict:
				print("invalid code. Try Again")
				continue
			else:
				print("invalid quantity. Try Again")
	return code_list

########################################################################################

def print_order_details(quantities):
	print("""\n\n-------------------------------------------------
ORDER DETAILS
-------------------------------------------------""")
	count=1
	total=0
	for i in range(10):
		if quantities[i]==0:
			continue
		else:
			print(f"[{count}] {dict[i][0]}*{quantities[i]} = Rs {dict[i][2]}*{quantities[i]} = Rs {dict[i][2]*quantities[i]}")
			count+=1
			total+=dict[i][2]*quantities[i]
	print(f"\nTOTAL COST = {total}")

########################################################################################

def calculate_category_wise_cost(quantities):
	print("""\n\n-------------------------------------------------
CATEGORY-WISE COST
-------------------------------------------------""")
	apparels_cost=0
	electronics_cost=0
	eatables_cost=0
	for i in range(10):
		if quantities[i]==0:
			continue
		else:
			if dict[i][1]=='Apparels':
				apparels_cost+=quantities[i]*dict[i][2]
			elif dict[i][1]=='Electronics':
				electronics_cost+=quantities[i]*dict[i][2]
			else:
				eatables_cost+=quantities[i]*dict[i][2]
	if apparels_cost!=0:
		print(f"Apparels = Rs {apparels_cost}")
	if electronics_cost!=0:
		print(f"Electronics = Rs {electronics_cost}")
	if eatables_cost!=0:
		print(f"Eatables = Rs {eatables_cost}")
	return (apparels_cost,electronics_cost,eatables_cost)

########################################################################################

def get_discount(cost, discount_rate):
	return int(cost * discount_rate)

########################################################################################

def calculate_discounted_prices(apparels_cost, electronics_cost, eatables_cost):
	print("""\n\n-------------------------------------------------
DISCOUNTS
-------------------------------------------------""")
	total=apparels_cost+electronics_cost+eatables_cost
	discount=0
	if apparels_cost>=2000:
		discounted_apparels_cost=apparels_cost-get_discount(apparels_cost,0.1)
		print(f"[APPARELS] Rs {apparels_cost} - Rs {get_discount(apparels_cost,0.1)} = Rs {discounted_apparels_cost}")
		discount+=get_discount(apparels_cost,0.1)
	else:
		discounted_apparels_cost=apparels_cost
	if electronics_cost>=25000:
		discounted_electronics_cost=electronics_cost-get_discount(electronics_cost,0.1)
		print(f"[ELECTRONICS] Rs {electronics_cost} - Rs {get_discount(electronics_cost,0.1)} = Rs {discounted_electronics_cost}")
		discount+=get_discount(electronics_cost,0.1)
	else:
		discounted_electronics_cost=electronics_cost
	if eatables_cost>=500: 
		discounted_eatables_cost=eatables_cost-get_discount(eatables_cost,0.1)
		print(f"[EATABLES] Rs {eatables_cost} - Rs {get_discount(eatables_cost,0.1)} = Rs {discounted_eatables_cost}")
		discount+=get_discount(eatables_cost,0.1)
	else:
		discounted_eatables_cost=eatables_cost
	print(f"\nTOTAL DISCOUNT = {discount}")
	print(f"TOAL COST = {total-discount}")
	return (discounted_apparels_cost,discounted_electronics_cost,discounted_eatables_cost)

########################################################################################

def get_tax(cost, tax):
	return int(cost * tax)

########################################################################################
def calculate_tax(apparels_cost, electronics_cost, eatables_cost):
	print("""\n\n-------------------------------------------------
TAX
-------------------------------------------------""")
	
	print(f"[APPARELS] Rs {apparels_cost} * 0.10 = Rs {get_tax(apparels_cost,0.10)}")
	print(f"[ELECTRONICS] Rs {electronics_cost} * 0.15 = Rs {get_tax(electronics_cost,0.15)}")
	print(f"[EATABLES] Rs {eatables_cost} * 0.05 = Rs {get_tax(eatables_cost,0.05)}")
	total_tax=get_tax(apparels_cost,0.10)+get_tax(electronics_cost,0.15)+get_tax(eatables_cost,0.05)
	total_cost_including_tax=apparels_cost+electronics_cost+eatables_cost+total_tax
	print(f"TOTAL TAX = {total_tax}")
	print(f"TOTAL COST = {total_cost_including_tax}")	
	return (total_cost_including_tax, total_tax)

########################################################################################

def apply_coupon_code(total_cost):
	
	coupon_discount=0
	print("""\n\n-------------------------------------------------
COUPON CODE
-------------------------------------------------""")
	while True:
		s=input("Enter coupon code (else leave blank): ")
		if s=='':
			print("No coupon code applied.")
			break
		elif s=='HELLE25':
			if total_cost>=25000:
				coupon_discount+=min(5000,0.25*total_cost)
				break
			else:
				break
		elif s=='CHILL50':
			if total_cost>=50000:
				coupon_discount+=min(10000,0.50*total_cost)
				break
			else:
				break
		else:
			print("Invalid coupon code. Try again.")
	total_cost_after_coupon_discount=total_cost-coupon_discount
	print(f"\nTOTAL COUPON DISCOUNT = Rs {coupon_discount}")
	print(f"TOTAL COST = Rs {total_cost_after_coupon_discount}")
	return (total_cost_after_coupon_discount,coupon_discount)
########################################################################################
def main():
	
	show_menu()
	ch='p'
	while ch!='n' and ch!='N' and ch!='Y' and ch!='y':
		ch=input("\nWould you like to buy in bulk? ( y or Y / n or N ): ")
	if ch=='n' or ch=='N':
		code_list=get_regular_input()
	else:
		code_list=get_bulk_input()
	print_order_details(code_list)
	category_wise_cost=calculate_category_wise_cost(code_list)  # TUPLE having 3 integers for 3 categories
	discounted_prices=calculate_discounted_prices(category_wise_cost[0],category_wise_cost[1],category_wise_cost[2]) # TUPLE of dicounted prices
	after_tax=calculate_tax(discounted_prices[0],discounted_prices[1],discounted_prices[2]) #TUPLE tax included total cost,total tax
	after_coupon=apply_coupon_code(after_tax[0])          # TUPLE 2 integers cost_after_coupon, coupon_discount
	print("\n\nThank You for visiting!")

########################################################################################

if __name__ == '__main__':
	main()
