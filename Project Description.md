=======  **WELCOME TO ONLINE SUPERMARKET PROJECT**  =======


In this initiative, we will be coding an online supermarket simulator in the Python programming language.

1. **OBJECTIVE** - To showcase the complete information about all products for sale to the customer. After that, depending upon the type* of the customer, the simulator will record the order in an organized manner. It would internally handle discounts on products (depends on what is the net final order). It would also take care of whether or not the customer avails coupon discount.

2. **KEY FEATURES** 

=> **Customer** **type**: There are two types of customers who visit the supermarket that is, a "_bulk buyer_" or a _"regular buyer_".

A "_regular buyer_" will have to enter the code of each product he wants to purchase and also at every selection, that is a selection input - [1 3 4 1] means that he selected the product with code '1' twice.

A "_bulk buyer_" will have to enter the quantity along with the item code while entering the order details.

=> **Discounts**: 

( before Taxation )

Apparels: 10% off if the base amount of Apparels before taxes ≥ 2000

Electronics: 10% off if base amount of Electronics before taxes ≥ 25000  Eatables: 10% off if the base amount of Eatables before taxes ≥ 500

( after Taxation )

Apparels: 10% on the cost of apparels after discount 

Electronics: 15% on the cost of electronics after discount 

Eatables: 5% on the cost of eatables after discount 

=>**Coupon discount** ( coupon is case sensitive )

_HELLE25_: The terms and conditions of HELLE25 are as follows:
-> It is valid only if the cost after discounts and taxes is ≥ 25000
-> It offers a discount of 25%, up to Rs. 5000

_CHILL50_   The terms and conditions are as follows:
-> It is valid only if the cost after discounts and taxes is ≥ 50000
-> It offers a discount of 50%, up to Rs. 10000

Note: As this is an interactive simulator, we will also be handling exception cases like- invalid item code, invalid coupon code, the invalid format of entering order details based on the type of customer.

" **Run the simulator to visit one of the best supermarkets and buy some stuff. Do not forget to use the coupon. Happy shopping!**__ "
