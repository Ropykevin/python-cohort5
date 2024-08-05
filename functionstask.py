# TASK 10: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that calculates the total stock in a company from the array/list below if we know that the stock is the last digit in every array/list.

# prods = [[‘omo’, ’30kshs’, ’300’], [‘milk’, ’50kshs’, ’200’], [‘bread’, ’45kshs’, ’359’], [‘coffee’, ’5kshs’, ’79’]]

# NB: ONCE YOU COPY AND PASTE THE LIST ABOVE, REWRITE THE SINGLE QUOTES AS THE ABOVE LIST WILL GIVE YOU AN ERROR.

prods = [['omo', '30kshs', '300'], ['milk', '50kshs', '200'], ['bread', '45kshs', '359'], ['coffee', '5kshs', '79'],["salt","60ksh","100"]]

def calc_stock():
    total_stock=0
    for prod in prods:
        stock=int(prod[-1])
        total_stock+=stock
    print(f"the total stock is {total_stock}")
        
calc_stock()