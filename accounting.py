melon_cost = 1.00

def price_comparison(file_path):
    """Function takes list of customers and compares price paid to price expected"""

    log = open(file_path)   #opens path to file

    for line in log:        #iterates over file
        line = line.rstrip()    #strips white space from right side
        words = line.split('|')     #splits string by delimiter '\'
        customer_name = words[1]    #chooses customer name 
        customer_melons = float(words[2])   #chooses and converts # of melons purchased
        customer_paid = float(words[3])     #chooses and converts price paid

    expected_amount = customer_melons * melon_cost  #calculates expected amount based on cost and # of melons

    if customer_paid != expected_amount:        #if customer paid a different amount that expected
        print(f"{customer_name} paid ${customer_paid:.2f},",    #print statement to compare expected vs paid amount
          f"expected ${expected_amount:.2f}"
          )

price_comparison("customer-orders.txt") #calls function on 'customer-orders.txt"

"""OLD CODE to be replaced
customer1_name = "Joe"
customer1_melons = 5
customer1_paid = 5.00

customer2_name = "Frank"
customer2_melons = 6
customer2_paid = 6.00

customer3_name = "Sally"
customer3_melons = 3
customer3_paid = 3.00

customer4_name = "Sean"
customer4_melons = 9
customer4_paid = 9.50

customer5_name = "David"
customer5_melons = 4
customer5_paid = 4.00

customer6_name = "Ashley"
customer6_melons = 3
customer6_paid = 2.00

customer1_expected = customer1_melons * melon_cost
if customer1_expected != customer1_paid:
    print(f"{customer1_name} paid ${customer1_paid:.2f},",
          f"expected ${customer1_expected:.2f}"
          )

customer2_expected = customer2_melons * melon_cost
if customer2_expected != customer2_paid:
    print(f"{customer2_name} paid ${customer2_paid:.2f},",
          f"expected ${customer2_expected:.2f}"
          )

customer3_expected = customer3_melons * melon_cost
if customer3_expected != customer3_paid:
    print(f"{customer3_name} paid ${customer3_paid:.2f},",
          f"expected ${customer3_expected:.2f}"
          )

customer4_expected = customer4_melons * melon_cost
if customer4_expected != customer4_paid:
    print(f"{customer4_name} paid ${customer4_paid:.2f},",
          f"expected ${customer4_expected:.2f}"
          )

customer5_expected = customer5_melons * melon_cost
if customer5_expected != customer5_paid:
    print(f"{customer5_name} paid ${customer5_paid:.2f},",
          f"expected ${customer5_expected:.2f}"
          )

customer6_expected = customer6_melons * melon_cost
if customer6_expected != customer6_paid:
    print(f"{customer6_name} paid ${customer6_paid:.2f},",
          f"expected ${customer6_expected:.2f}"
          )
"""