from OOPModule_ER import FancyFood_ER

def OrderProduct_ER():
    product_list = []
    product_amount = input("How many items will you order today?: ")

    #prompt users to enter the number of items
    while product_amount.isdigit() == False:
        product_amount = input("Invalid input. Number of items must be at least 1. How many items will you order today?: ")

    product_amount = int(product_amount)
    while product_amount < 1:
        print("Number of items must be at least 1.")
        product_amount = input("How many items will you order today?: ")
    

    for i in range(0, product_amount):
        print(f"Items #{i+1}")
        product_name = input("Enter food: ")
        product_pounds = input("Enter amount of pounds: ")
        print()

        #prompt users to enter the number of pounds
        product_pounds = float(product_pounds)
        while product_pounds <= 0 :
            print("Amount of pounds must be greater than 0.")
            product_pounds = float(input("Enter amount of pounds: "))
        
        product_list.append(FancyFood_ER(product_name, product_pounds))
    
    return product_list


def DisplayProducts_ER(product_list):
    print("\nHere's a summary of the items purchased:")
    print("--------------------------------------------------")

    for product in product_list:
        print(product.__str__())
        print()


def CalculateTotal_ER(product_list):
    total_cost = 0.00
    for product in product_list:
        total_cost += (product.calculate_price_ER())
    return f"Total cost: ${total_cost:.2f}"


order_list = OrderProduct_ER()
DisplayProducts_ER(order_list)
print(CalculateTotal_ER(order_list))
